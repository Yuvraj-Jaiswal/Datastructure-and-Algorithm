
class Vertex:

    def __init__(self,key):
        self.key = key
        self.connected_to = {}

    def add_Neighbour(self,key,weight=0):
        self.connected_to[key] = weight

    def get_weight(self,key):
        return self.connected_to[key]

    def conected_to(self):
        return self.connected_to.keys()

    def return_keys(self):
        return self.key

    def __str__(self):
        return str(self.key) + "  conected to  "


class Graph:

    def __init__(self):
        self.vert_list = {}
        self.vert_count = 0

    def get_vertex(self,n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def add_vertex(self,key):
        self.vert_count += 1
        vert = Vertex(key)
        self.vert_list[key] = vert
        return vert

    def add_edge(self,f,t,cost=0):
        if f not in self.vert_list:
            self.add_vertex(f)

        if t not in self.vert_list:
            self.add_vertex(t)

        self.vert_list[f].add_Neighbour(t,cost)

    def return_vertex(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())

    def __contains__(self, n):
        return n in self.vert_list








