N = int(input())
T, M = map(int, input().rstrip().split(" "))
c = [int(input()) for _ in range(N)]

allTime = sum(c)
hour = allTime // 60
minute = allTime % 60

allMin = M + minute
allTime = T + hour

if allMin >= 60:
		allTime += 1
		allMin -= 60

print(allTime % 24, allMin)
