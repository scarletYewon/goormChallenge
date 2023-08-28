# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
input = sys.stdin.readline

N,K = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(N)]

def solution(N,K, graph):
	answer = 0
	dy = [-1, 1, 0, 0, -1, -1, 1, 1]
	dx = [0, 0 , -1, 1, -1 ,1, -1, 1]
	
	for row in range(N):
		for col in range(N):
			if graph[row][col] == 1:
				continue
				
			count = 0
			for i in range(8):
				next_y = row + dy[i]
				next_x = col + dx[i]
				
				if 0 <= next_y < N and 0 <= next_x < N and graph[next_y][next_x] == 1: 
					count += 1
					
			if count == K:
				answer += 1
	
	print(answer)
	return

solution(N,K, graph)