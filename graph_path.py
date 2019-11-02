graph ={ 
'a':['b', 'd', 'e'], 
'b':['c'], 
'c':['d', 'e'], 
'd':['c', 'e'], 
'e':['b'] 
} 

def find_path(graph, start, end, path =[]): 
  path = path + [start] 
  if start == end: 
    return path 
  for node in graph[start]: 
    if node not in path: 
      newpath = find_path(graph, node, end, path) 
      if newpath:  
        return newpath 
      return None

print(find_path(graph, 'd', 'c')) 
