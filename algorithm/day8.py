# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
bandage = 1
medicine = 7
painkiller = 14
cnt = 0


if n//14 ==0:
	if n//7 == 0:
		print(n)
	else:
		cnt += n//7
		n %=7
		cnt +=n
		print(cnt)
else:
	cnt += n//14
	n %=14
	cnt += n//7
	n %=7
	cnt +=n
	print(cnt)
	
