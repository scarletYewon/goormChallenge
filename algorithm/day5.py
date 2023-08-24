N, K = map(int, input().split())

def f(x):
	x = int(x)
	bin_count = bin(x).count('1')	
	return bin_count, x

nums = list(map(f, input().split()))
nums.sort(reverse=True)
print(nums[K - 1][1])