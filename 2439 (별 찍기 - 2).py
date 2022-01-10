# <2439>

# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제 (우측정렬)

# 1
a = int(input())

for N in range(1, a+1):
    print(('*' * N).rjust(a))

# 2
N = int(input())

for i in range(1, N+1):
    print(" " * (N-i) + "*" * i)
