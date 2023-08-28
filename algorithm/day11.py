# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from sys import stdin

k = int(input())

a,b = map(int, stdin.readline().split())

li =[a,b]


dp = [1000001] * (k+1)
dp[0] = 0

for num in li:
   for i in range(num, k+1):
       dp[i] = min(dp[i],dp[i-num]+1)
if dp[k] == 1000001:
   print(-1)
else:
   print(dp[k])
	