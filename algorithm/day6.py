N = int(input())
S = input()

# 부분 문자열 집합 구하기
P = set()

for idx in range(N):
	for i in range(1, N - 1):
		P.add(S[idx:idx+i])

scores = {p: idx + 1 for idx, p in enumerate(sorted(list(P)))}

# DFS
max_score = 0
stack = [(S, 0, 0)]
while stack:
	text, step, score = stack.pop()
    # 3번째 부분 문자열일 때, 점수 계산 및 최고 점수 갱신
	if step == 2:
		try:
			score += scores[text]
		except KeyError:
			pass
		else:
			max_score = max(max_score, score)
		finally:
			continue
	
    # 1~2번째 문자열일 때, 다음 단계 진행
	for i in range(1, N - 1):
		p = text[:i]
		if not p:
			continue
		stack.append((text[i:], step + 1, score + scores[p]))
		
print(max_score)