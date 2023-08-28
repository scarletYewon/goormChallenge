# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

input = sys.stdin.readline

N = int(input())  # 보드의 크기
goorm_Y, goorm_X = map(int, input().split(" "))  # goorm의 시작 위치
player_Y, player_X = map(int, input().split(" "))  # 플레이어의 시작 위치
query_board = [input().rstrip().split(" ") for _ in range(N)]  # 보드에 대한 쿼리

# 인덱스 조정
goorm_Y -= 1
goorm_X -= 1
player_Y -= 1
player_X -= 1

# 인덱스 범위가 넘어갔을 때 조정하는 함수
def change(index, N):
    if index < 0:
        index = N + (index % N)
    if index >= N:
        index = index % N
    return index

# 주어진 방향으로 이동하는 함수
def move(Y, X, visited, N):
    queries = {
        "L": (0, -1),  # 왼쪽
        "R": (0, 1),   # 오른쪽
        "U": (-1, 0),  # 위쪽
        "D": (1, 0),   # 아래쪽
    }
    move_count = int(query_board[Y][X][0: len(query_board[Y][X]) - 1])  # 이동할 횟수
    dy, dx = queries.get(query_board[Y][X][-1])  # 이동할 방향

    for i in range(move_count):
        Y = change(Y + dy, N)  # Y 좌표 변경
        X = change(X + dx, N)  # X 좌표 변경

        if (Y, X) not in visited:
            visited.append((Y, X))
        else:
            return Y, X, False

    return Y, X, True
	
	# 해결책 함수
def solution(N, goorm_Y, goorm_X, player_Y, player_X):
    goorm_visited = [(goorm_Y, goorm_X)]  # goorm이 방문한 경로
    player_visited = [(player_Y, player_X)] # 플레이어가 방문한 경로

    goorm_flag = True
    player_flag = True

    while goorm_flag:  # goorm 이동
        goorm_Y, goorm_X, goorm_flag = move(goorm_Y, goorm_X, goorm_visited, N)

    while player_flag:  # 플레이어 이동
        player_Y, player_X, player_flag = move(player_Y, player_X, player_visited, N)

    # 방문한 경로 수 비교
    if len(goorm_visited) > len(player_visited):
        print("goorm", len(goorm_visited))
    else:
        print("player", len(player_visited))

    return

# 함수 호출
solution(N, goorm_Y, goorm_X, player_Y, player_X)