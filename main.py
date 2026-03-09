import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

class SaborExpressDelivery:
    def __init__(self, num_nodes=50, num_deliveries=15, num_drivers=3):
        self.num_nodes = num_nodes
        self.num_deliveries = num_deliveries
        self.num_drivers = num_drivers
        self.graph = nx.Graph()
        self.pos = {}
        self.delivery_nodes = []
        self.hub_node = 0 
        
    def generate_city_graph(self):
       
        seed = 42 
        np.random.seed(seed)
        
        positions = np.random.rand(self.num_nodes, 2)
        for i in range(self.num_nodes):
            self.pos[i] = positions[i]
            self.graph.add_node(i, pos=positions[i])
            
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                dist = np.linalg.norm(positions[i] - positions[j])
                if dist < 0.25:
                    self.graph.add_edge(i, j, weight=dist)
        
        if not nx.is_connected(self.graph):
            components = list(nx.connected_components(self.graph))
            for k in range(len(components) - 1):
                u = list(components[k])[0]
                v = list(components[k+1])[0]
                dist = np.linalg.norm(self.pos[u] - self.pos[v])
                self.graph.add_edge(u, v, weight=dist)

    def select_deliveries(self):
        candidates = list(range(1, self.num_nodes))
        self.delivery_nodes = np.random.choice(candidates, self.num_deliveries, replace=False)
        print(f"📍 Locais de Entrega: {self.delivery_nodes}")

    def cluster_deliveries(self):
        delivery_coords = [self.pos[n] for n in self.delivery_nodes]
        
        kmeans = KMeans(n_clusters=self.num_drivers, random_state=42, n_init=10)
        labels = kmeans.fit_predict(delivery_coords)
        
        clusters = {i: [] for i in range(self.num_drivers)}
        for node, label in zip(self.delivery_nodes, labels):
            clusters[label].append(node)
            
        return clusters

    def heuristic(self, u, v):
        pos_u = self.pos[u]
        pos_v = self.pos[v]
        return np.linalg.norm(pos_u - pos_v)

    def optimize_routes(self, clusters):
        final_routes = {}
        
        for driver_id, nodes in clusters.items():
            if not nodes:
                continue
            current_node = self.hub_node
            unvisited = nodes.copy()
            route_path = [current_node]
            full_path_edges = []
            
            while unvisited:
                next_node = min(unvisited, key=lambda x: np.linalg.norm(self.pos[current_node] - self.pos[x]))
                
                try:
                    path_segment = nx.astar_path(self.graph, current_node, next_node, heuristic=self.heuristic, weight='weight')
                    
                    if len(route_path) > 1:
                        route_path.extend(path_segment[1:])
                    else:
                        route_path.extend(path_segment[1:])
                        
                    for k in range(len(path_segment) - 1):
                        full_path_edges.append((path_segment[k], path_segment[k+1]))
                        
                    current_node = next_node
                    unvisited.remove(next_node)
                except nx.NetworkXNoPath:
                    print(f" Alerta: Sem caminho entre {current_node} e {next_node}")
                    unvisited.remove(next_node)
            

            try:
                path_home = nx.astar_path(self.graph, current_node, self.hub_node, heuristic=self.heuristic, weight='weight')
                route_path.extend(path_home[1:])
                for k in range(len(path_home) - 1):
                    full_path_edges.append((path_home[k], path_home[k+1]))
            except:
                pass

            final_routes[driver_id] = {
                "sequence": route_path,
                "edges": full_path_edges
            }
            
        return final_routes

    def visualize(self, routes):
        plt.figure(figsize=(10, 8))
        
        nx.draw(self.graph, self.pos, with_labels=False, node_size=20, node_color='lightgray', edge_color='gray', alpha=0.4)
        
        nx.draw_networkx_nodes(self.graph, self.pos, nodelist=[self.hub_node], node_color='black', node_size=150, label="Restaurante (Hub)")
        
        colors = ['red', 'blue', 'green', 'orange', 'purple']
        
        for driver_id, data in routes.items():
            color = colors[driver_id % len(colors)]
            
            nx.draw_networkx_edges(self.graph, self.pos, edgelist=data['edges'], edge_color=color, width=2, label=f"Motorista {driver_id+1}")
            
            driver_deliveries = [n for n in data['sequence'] if n in self.delivery_nodes]
            nx.draw_networkx_nodes(self.graph, self.pos, nodelist=driver_deliveries, node_color=color, node_size=80)

        plt.title("Otimização de Rotas - Sabor Express (K-Means + A*)")
        plt.legend()
        plt.show()

if __name__ == "__main__":
    print("Iniciando Sistema Sabor Express AI...")
    
    app = SaborExpressDelivery(num_nodes=60, num_deliveries=12, num_drivers=3)
    
    app.generate_city_graph()
    
    app.select_deliveries()
    
    clusters = app.cluster_deliveries()
    print("\n📦 Agrupamento (Clusters):")
    for d, nodes in clusters.items():
        print(f"  Motorista {d+1}: {len(nodes)} entregas -> Nós {nodes}")
    
    routes = app.optimize_routes(clusters)
    
    app.visualize(routes)
    print("\n Otimização Concluída. Mapa gerado.")