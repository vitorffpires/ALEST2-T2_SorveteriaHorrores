from digraph import Digraph

class DFS:

    def __init__(self, Digraph, s):
        self.Digraph = Digraph
        self.s = 0

        self.marked = [False] * len(Digraph.verts)
        self.edgeTo = [-1] * len(Digraph.verts)

        self.dfs(s)

    def dfs(self, v):
        self.marked[v] = True
        for w in self.Digraph.adj(v):
            if not self.marked[w]:
                self.edgeTo[w] = v
                self.dfs(w)

    def hasPathTo(self, v):
        return self.marked[v]

    def pathTo(self, w):
        if not self.hasPathTo(w):
            return None
        path = []
        while w != self.s:
            path.insert(0,w)
            w = self.edgeTo[w]
        path.insert(0,self.s)
        return path

        
if __name__ == "__main__":

    g = Digraph('casos_cohen_t2/casocohen60.txt')
    #g = Digraph()

    #g.addEdge(0, 2);
    #g.addEdge(2, 1);
    #g.addEdge(2, 4);
    #g.addEdge(1, 3);
    #g.addEdge(3, 4);

    g.toDot()

    dfs = DFS(g, 0)

    for v in range(g.totalVerts):
        if dfs.hasPathTo(v):
            print(f"{v}: {dfs.pathTo(v)}")


