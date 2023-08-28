import sys

input = sys.stdin.readline

dlist = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]

def main():
	n, k = map(int, input().split())
	matrix = [list(input().split()) for _ in range(n)]
	
	dp = [[0]*n for _ in range(n)]
	
	for _ in range(k):
		i, j = map(int, input().split())
		i -= 1
		j -= 1
		for dx, dy in dlist:
			if 0 <= (di:=i+dx) < n and 0 <= (dj:=j+dy) < n:
				if matrix[di][dj] == '#':
					continue
				elif matrix[di][dj] == '@':
					dp[di][dj] += 2
				elif matrix[di][dj] == '0':
					dp[di][dj] += 1
					
	print(max([max(d) for d in dp]))	
	
main()