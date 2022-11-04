from digraph import Digraph
from dfs import DFS

if __name__ == "__main__":
    
    g = Digraph()
    
    #g = Digraph()

    
    g.addEdge("amendoim", "coco_queimado")
    g.addEdge("menta", "creme_russo")
    g.addEdge("menta", "chiclete")
    g.addEdge("queijo", "creme_russo")
    g.addEdge("queijo", "morango_e_nata")
    g.addEdge("queijo", "chiclete")
    g.addEdge("abóbora", "coco_queimado")
    g.addEdge("abóbora", "chiclete")
    g.addEdge("creme_russo", "coco_queimado")
    g.addEdge("creme_russo", "pitanga")
    g.addEdge("creme_russo", "morango_e_nata")
    g.addEdge("pitanga", "morango_e_nata")
    g.addEdge("morango_e_nata", "chiclete")
    g.addEdge("limão", "queijo")
    g.addEdge("limão", "abóbora")
    g.addEdge("limão", "coco_queimado")
    g.addEdge("limão", "pitanga")

    

    #dfs = DFS(g,0)

    g.toDot()
