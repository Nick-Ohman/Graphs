class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)
        

    def get_parents(self, vertex):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex]
       

    ## Build a path like we did in search
    ## But we dont know when to stop until weve seen everyone
graph = Graph()
def build_graph(ancestors):
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
    return graph





    


def earliest_ancestor(ancestors, starting_node):
    
    graph = build_graph(ancestors)

    s = Stack()

    visited = set()

    s.push([starting_node])

    longest_path = []
    aged_one = -1

    while s.size() > 0:

        path = s.pop()
        current_node = path[-1]


        # if path is longer, or path is equal but the id is smaller
        if len(path) > len(longest_path) or (len(path) == len(longest_path) and current_node < aged_one):
            longest_path = path
            aged_one = longest_path[-1]

        if current_node not in visited:
            visited.add(current_node)

            parents = graph.get_parents(current_node)

            for parent in parents:
                new_path = path + [parent]
                s.push(new_path)
    
    return longest_path[-1]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # visited = set()

    # q = Queue()
    # q.enqueue([starting_node])

    # while q:
    #     path = q.dequeue()

    #     vertex = path[-1]

    #     for ancestor in ancestors(vertex):
    #         if ancestor[1] == vertex:
    #             new_path = list(path)
    #             new_path.append(ancestor[0])
    #             q.enqueue(new_path)
    #         visited.add(vertex)
    # return
    
    # vertices = {}

    # for parent, child in ancestors:
    #     #checking if parent is not in vert
    #     # we'll set the parnets key to value of child
    #     if parent not in vertices:
    #         vertices[parent] = [child]

    # q = Queue()
    # q.enqueue([starting_node])

    # #while the q is not empty
    # while q.size() > 0:

    #     #dequeu the first path
    #     path = q.dequeue()
        

    #     #if not parents return -1
    #     if starting_node
    #     #otherwise pass them into the 
    #     #q if their are mulit parents and add the lowest one

    #     #once no parents print that value

 
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 1))


        
    
        


    