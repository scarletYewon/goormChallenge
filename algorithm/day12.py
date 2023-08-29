from collections import deque

n = int(input())

village = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
	return 0 <= x < n and 0 <= y < n

def bfs(i, j):
	queue = deque([(i, j)])
	visited[i][j] = True
	while queue:
		x, y = queue.popleft()
		for dx, dy in zip(dxs, dys):
			nx, ny = x + dx, y + dy
			if in_range(nx, ny) and not visited[nx][ny] and village[nx][ny]:
				queue.append((nx, ny))
				visited[nx][ny] = True

answer = 0
for i in range(n):
	for j in range(n):
		if not visited[i][j] and village[i][j]:
			bfs(i, j)
			answer += 1

print(answer)