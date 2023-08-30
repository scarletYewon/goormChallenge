import sys
from collections import deque

input = sys.stdin.readline

def main():
	n, k = map(int, input().split())
	matrix = [list(map(int, input().split())) for _ in range(n)]
	village = [0]*31
	visited = [[False]*n for _ in range(n)]
	
	def bfs(x, y):
		visited[x][y] = True
		
		q = deque([(x, y)])
		
		count = 0
		
		while q:
			i, j = q.popleft()
			count += 1
			for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
				if 0 <= (di:=i+dx) < n and 0 <= (dj:=j+dy) < n and matrix[di][dj] == matrix[x][y] and not visited[di][dj]:
					visited[di][dj] = True
					q.append((di, dj))
					
		return count >= k
	
	for i in range(n):
		for j in range(n):
			if not visited[i][j]:
				if bfs(i, j):
					village[matrix[i][j]] += 1
				
	max_val = 0
	max_idx = 1
	for i in range(31):
		if village[i] >= max_val:
			max_val = village[i]
			max_idx = i
	print(max_idx)
	
main()