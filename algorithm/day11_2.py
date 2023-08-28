def	main():
	N = int(input())
	A, B = map(int, input().split())
	A, B = max(A, B), min(A, B)

	a = N // A
	b = (N - a * A) // B
	while a * A + b * B != N:
		a -= 1
		b = (N - a * A) // B
		if a < 0:
			print(-1)
			return
	print(a + b)

if __name__ == "__main__":
	main()