Nodes = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)

Edges = [(0, 5, {'weight': 1}), (0, 7, {'weight': 9}), (0, 11, {'weight': 11}),
        (0, 16, {'weight': 11}), (0, 17, {'weight': 3}), (0, 18, {'weight': 9}),
        (1, 5, {'weight': 5}), (1, 7, {'weight': 1}), (1, 9, {'weight': 10}),
        (1, 15, {'weight': 1}), (1, 16, {'weight': 6}), (1, 19, {'weight': 12}),
        (2, 12, {'weight': 14}), (2, 16, {'weight': 4}), (2, 19, {'weight': 13}),
        (3, 7, {'weight': 5}), (3, 15, {'weight': 1}), (3, 16, {'weight': 10}),
        (3, 18, {'weight': 4}), (4, 7, {'weight': 3}), (4, 8, {'weight': 11}),
        (4, 11, {'weight': 12}), (4, 13, {'weight': 13}), (4, 16, {'weight': 9}),
        (4, 18, {'weight': 8}), (5, 7, {'weight': 2}), (5, 8, {'weight': 2}),
        (5, 9, {'weight': 13}), (5, 11, {'weight': 1}), (5, 14, {'weight': 12}),
        (6, 7, {'weight': 8}), (6, 10, {'weight': 6}), (6, 13, {'weight': 13}),
        (6, 15, {'weight': 5}), (6, 18, {'weight': 13}), (7, 8, {'weight': 2}),
        (7, 11, {'weight': 13}), (7, 16, {'weight': 4}), (7, 17, {'weight': 6}),
        (7, 19, {'weight': 7}), (8, 13, {'weight': 8}), (8, 14, {'weight': 10}),
        (8, 16, {'weight': 14}), (9, 16, {'weight': 9}), (10, 17, {'weight': 7}),
        (10, 19, {'weight': 5}), (11, 13, {'weight': 12}), (11, 14, {'weight': 13}),
        (11, 15, {'weight': 2}), (12, 13, {'weight': 9}), (12, 15, {'weight': 7}),
        (12, 17, {'weight': 8}), (13, 15, {'weight': 1}), (13, 18, {'weight': 9}),
        (13, 19, {'weight': 6}), (14, 18, {'weight': 9}), (15, 18, {'weight': 2}),
        (17, 18, {'weight': 14}), (17, 19, {'weight': 13})]

#Define a big enough number to distinguish between valid weights.
intmax = 999999999

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def fill_Matrix(self):
        for edge in Edges:
            g.graph[ edge[0] ][ edge[1] ] = edge[2]["weight"]
            g.graph[ edge[1] ][ edge[0] ] = edge[2]["weight"]

    # Print the Adjacent Matrix to validate the correctness of the fillment.
    def printMatrix(self):
        for node in Nodes:
            print(self.graph[node])
        
    def printShortestDistances(self, distance, source):
        print("Vertex \tDistance from Source", source)
        for node in range(self.V):
            print(node, "\t", distance[node])

# Find the the minimum value in distance list that has not been visited yet
# Fill the visitedOrder list
    def minDistanceEdge(self, distance, visitedMarking, visitedOrder):
        min = intmax
        min_index = None
        for vertix in range(self.V):
            if distance[vertix] < min and visitedMarking[vertix] == False:
                min = distance[vertix]
                min_index = vertix
        visitedOrder.append( min_index )
        # Return the vertix in which the minimum distance is found
        return min_index

# Dijkstra Algorithm
    def dijkstra_ALGA(self, source, destination):
        # List of infinite values of distance
        distance = [intmax] * self.V
        # Mark the starting point to be 0th vertix
        distance[source] = 0
        # List to mark the visited vertices
        visitedMarking = [False] * self.V
        # List of visited vertices.
        visitedOrder = []
        # Immediate source list
        immSrc = [0] * self.V

        path = []

        # Iterate over all the vertices
        for vertix in range(self.V):
            # Place the pointer at the vertix which has the current minimum distance
            pointer = self.minDistanceEdge(distance, visitedMarking, visitedOrder)
            # Mark the vertix with the minimum distance as visited
            visitedMarking[pointer] = True

            # Iterate over the distances
            for edge_weight in range(self.V):
                # If the distance is not zero
                if self.graph[pointer][edge_weight]:
                    # Calculate the overall distance from the current pointer
                    # to the edge
                    overall_distance = distance[pointer] + \
                                       self.graph[pointer][edge_weight]
                    # If the distance is less than the current distance
                    # Update the distance with the shortest
                    if visitedMarking[edge_weight] == False and \
                       distance[edge_weight] > overall_distance:
                        distance[edge_weight] = overall_distance
                        immSrc[edge_weight] =  pointer
                    #print(distance)
            #print(visitedMarking)
        # Print the results
        self.printShortestDistances(distance, source)
        #print("Visited Order:",visitedOrder, sep="\n")
        #print("Immeadiate source:",immSrc, sep="\n")

        while( destination ):
            path.insert( 0, destination )
            destination = immSrc[destination]
        path.insert( 0, destination )
        print("Path of shortest distance from source to destination: ", path )
            
g = Graph(20)
g.fill_Matrix()
#g.printMatrix()
g.dijkstra_ALGA(0, 14)
