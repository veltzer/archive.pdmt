from pygraph.algorithms.filters.null import null
from sys import getrecursionlimit, setrecursionlimit

def depth_first_search_gen(graph):
    visited = set()
    notvisited = set()
    for each in graph:
        notvisited.add(each)
    while len(notvisited)>0:
        node=notvisited.pop()
	for each in graph[node]:
	    visitlist.

    for each in graph:
        if each not in visited:
            
	    for node in dfs(each):
	        yield node
