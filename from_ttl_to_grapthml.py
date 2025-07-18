from rdflib import Graph
import networkx as nx

# Carica il file RDF/XML o TTL
g = Graph()
g.parse(r"C:\Users\nadia\Desktop\Lisontology-\aligned_lisontology.ttl", format="turtle")

# Converti in grafo NetworkX
G = nx.DiGraph()
for s, p, o in g:
    G.add_edge(str(s), str(o), label=str(p))

# Salva in GraphML
nx.write_graphml(G, r"C:\Users\nadia\Desktop\Lisontology-\aligned_lisontology.graphml")