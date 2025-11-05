'''You are having social network system. Each user relates to different friends.  You must figure out the path between 2 persons
•	Example. User1 relates to User2 who relates to User3 who relates to User1
•	I prefer the shortest path but consider this as least priority
•	Sample data format is below.  Please have nested data format
{
“A”:  [“B”, “C”],
“B”:  [“A”, “D”, “E”],
“C”:  [“A”],
“D”: [“B”],
“E”: [“B”]
}
'''
from collections import deque

def connection(graph,startp,endp):
    q=deque([[startp]])
    visited=set()
    while q:
        path=q.popleft()
        if path[-1]==endp:
            return path
        if path[-1] not in visited:
            visited.add(path[-1])
            for other in graph[path[-1]]:
                pathnew=list(path)
                pathnew.append(other)
                q.append(pathnew)
    return "No path found"
    
graph={
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A"],
    "D": ["B"],
    "E": ["B"]
}

print(connection(graph,"C","D"))


