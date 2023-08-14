import math

W, R = map(int,input().split())
answer = W * (1+R/30) 
print(math.floor(answer))