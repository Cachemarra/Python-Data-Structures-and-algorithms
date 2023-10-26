# %% Constructors
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        # Evade duplicates
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])







# %% Tests

my_graph = Graph()
my_graph.add_vertex("A")
my_graph.print_graph()


# %%
