"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
                        

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        q = Queue()

        # Add starting vertex ID
        q.enqueue(starting_vertex)

        # Create set for visited verts
        visited = set()

        # While queue is not empty
        while q.size() > 0:

            # Dequeue a vert
            v = q.dequeue()

            # If not visited
            if v not in visited:

                # Visit it!
                print(v)

                # Mark as visited
                visited.add(v)

                # Add all neighbors to the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
    # make a Stack
        stack = Stack()
        # push on our starting node
        stack.push(starting_vertex)
        # make a set to track if we've been here before
        visited = set()
        # while our stack isn't empty
        while stack.size() > 0:
        # pop off whatever's on top this is our current_node
            current_node = stack.pop()
            if current_node not in visited:
                print(current_node)
        # if we haven't visited this vertex yet then mark as Visited
            if current_node not in visited:
                    visited.add(current_node)
        # get it's neighbors
                    neighbors = self.get_neighbors(current_node)    
        # for each of the neighbors add to the stack
                    for neighbor in neighbors:
                        if neighbor not in visited:
                            stack.push(neighbor)





    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)



        
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
       # create empty queue using the Queue class provided
        queue = [[starting_vertex]]
        # created empty set to house the visited nodes
        visited = []

        #return is start is dest
        if starting_vertex == destination_vertex:
            return queue

        # While the queue is not empty...
        while queue:
            # Dequeue the first PATH
            path= queue.pop(0)
            # Grab the last vertex from the PATH
            vertex = path[-1]
            # If that vertex has not been visited...
            if vertex not in visited:
                # Mark it as visited...
                for next_v in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(next_v)
                    queue.append(new_path)
                    if next_v == destination_vertex:
                        return new_path
                visited.append(vertex)
        return 
                    

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

         # create empty queue using the Queue class provided
        stack = [[starting_vertex]]
        # created empty set to house the visited nodes
        visited = []

        #return is start is dest
        if starting_vertex == destination_vertex:
            return stack

        # While the queue is not empty...
        while stack:
            # Dequeue the first PATH
            path=stack.pop(0)
            # Grab the last vertex from the PATH
            vertex = path[-1]
            # If that vertex has not been visited...
            if vertex not in visited:
                # Mark it as visited...
                for next_v in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(next_v)
                    stack.append(new_path)
                    if next_v == destination_vertex:
                        return new_path
                visited.append(vertex)
        return 
       

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if path is None:
            path = []

        visited.add(starting_vertex)

        #path = path + [starting_vertex] ## makes a copy of the path
        ## does the same thing as line above
        path = list(path) ## makes copy 
        path.append(starting_vertex)

        if starting_vertex == destination_vertex:
            return path

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if new_path is not None:
                    return new_path

        return None


       


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
