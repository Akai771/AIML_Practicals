#for DFS
from collections import defaultdict
class Graph:
    #constructor
    def __init__(self):
        #default dictionary to store graph
        self.graph=defaultdict(list)

    #function to add an edge to a graph
    def addEdge (self,u,v):
        self.graph[u].append(v)
        #print(u,self.graph[u])

    #function used by util
    def DFSutil (self,v, visited):
        #Mark current node as visited and print
        #print("inside dfsutil",v,end=" ")
        #print(visited,end=" ") 
        visited[v]= True
        print(v, end=" ")
        
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            #print(end"\n")
            #print("inside for ",i,visited[i])
            if visited[i]==False:
                self.DFSutil(i,visited)

    #function to do DFS Traversal. It usesrecursive DFSutil
    def DFS(self,v):
        #Matrk all the vertices as not visited
        visited=[False]*(len(self.graph))
        #print ("inside DFS")
        print(visited)
        #vcall the recursive function helper function to print DFS Traversal
        self.DFSutil(v,visited)

#creating Graph
g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print("Following is DFS starting from vertex 2")
g.DFS(2)