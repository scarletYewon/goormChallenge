# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(node, cnt):
	for next_node in adj[node]:
		if not visited[next_node]:
			visited[next_node] = True
			return dfs(next_node, cnt+1)
	return cnt, node

n, m, k = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
	s, e = map(int, input().split())
	adj[s].append(e)
	adj[e].append(s)

for i in range(1, n+1):
	adj[i].sort()
	
visited = [False]*(n+1)
visited[k] = True
	
print(* dfs(k, 1))