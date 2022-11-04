from ast import Pass


class Digraph:

    def __init__(self, filename=None):
        self.verts = {}
        self.totalEdges = 0
        self.two_comb_list = []
        self.thre_comb_list = []

        if filename:
            with open(filename) as f:
                lines = f.readlines()
                for v in lines:
                    v = v.split(" ")
                    self.addVert(v[0])
                    self.addVert(v[2])
                for e in lines:
                    line = e.split(" ")
                    #print(line[0])
                    #print(line[2].split('\n')[0])
                    v,w = line[0], line[2].split('\n')[0]
                    self.addEdge(v,w)

    def addVert(self, value):
        if value in self.verts: #se o valor ja esta no dicionario verts
            return              # retorna; se não,
        self.verts[value] = []  #cria lista vazia para o valor do vertice


    def addEdge(self, v1, v2):
        if v1 not in self.verts:
            self.addVert(v1)
        if v2 not in self.verts:
            self.addVert(v2)
        assert(v2 not in self.verts[v1])
        self.verts[v1].append(v2)
        self.totalEdges += 1

    def adj(self, v):
        if v not in self.verts:
            return None
        return self.verts[v]

    def print(self):
        print("Vertices:",len(self.verts))
        print("Edges:",self.totalEdges)
        for v in self.verts:
            print(f"{v}: ", end="")
            for w in self.verts[v]:
                print(f"{w} ", end="")
            print()

    def toDot(self):
        print("graph {")
        print("  rankdir = LR")
        print("  node [shape=circle]")
        # Precisa listar todos os vértices, pois pode não haver arestas!
        for v in self.verts:
            print(f"  {v};")
        # Agora lista as arestas
        for v in self.verts:
            for w in self.verts[v]:
                print(f"  {v} -> {w}")
        print("}")

    def caminha_dois(self,pai,filho):
        for i in self.verts[filho]:
            if(f"  {pai} -> {i}") not in self.two_comb_list:
                        self.two_comb_list.append(f"  {pai} -> {i}")
            self.caminha_dois(pai, i)

    def caminha_tres(self,pai,filho):
        for i in self.verts[filho]:
            for j in self.verts[i]:
                if(f"  {pai} -> {i} -> {j}") not in self.thre_comb_list:
                        self.thre_comb_list.append(f"  {pai} -> {i} -> {j}")
                self.caminha_tres(pai, j)
            self.caminha_tres(pai, i)
            

    def countLigDois(self):
        for v in self.verts: # para cada valor na lista
            self.caminha_dois(v,v) # chama funão auxiliar

    def countLigTres(self):
        for v in self.verts: # para cada valor na lista
            self.caminha_tres(v,v) # chama funão auxiliar

    def print_comb_dois(self):
        self.countLigDois() #construtor
        for i in self.two_comb_list:
            print(i)
        print("total de combinações", len(self.two_comb_list))

    def print_comb_tres(self):
        self.countLigTres() #construtor
        for i in self.thre_comb_list:
            print(i)
        print("total de combinações", len(self.thre_comb_list))


if __name__ == "__main__":

    g = Digraph('casos_cohen_t2/casocohen10.txt')
    #g = Digraph()
    #o de 60casos teve 4782 combinaões de três

    #g.addEdge(0, 2);
    #g.addEdge(2, 1);
    #g.addEdge(2, 4);
    #g.addEdge(1, 3);
    #g.addEdge(3, 4);

    #print(g.adj(2))

    g.print()
    print()

    g.toDot()


    #g.print_comb_dois()