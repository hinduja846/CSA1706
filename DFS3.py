from collections import deque
graph={'1':['2','7'],
       '2':['3','6'],
       '3':['4','5'],
       '4':[],
       '5':[],
       '6':[],
       '7':['8','10'],
       '8':['9'],
       '9':[],
       '10':[]
}
def dfs(start,visited=None):
    if visited is None:
       visited=[]
    visited.append(start)
    for node in graph[start]:
       if node not in visited:
           dfs(node,visited)
    return visited
print(dfs('1')) 
