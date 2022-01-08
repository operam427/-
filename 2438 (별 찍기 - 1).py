# < 2438번 > (별 찍기 - 1)

# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

# 1
a = int(input())

for N in range(1, a+1):
    print('*' * N)

# 2
a = int(input())

for N in range(a):
    print('*' * (N+1))
