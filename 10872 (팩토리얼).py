# <10872>

'''
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.
첫째 줄에 N!을 출력한다.
'''

# 1.
N = int(input())
num = 1

if N == 0:
    print(num)
else:
    for i in range(1, N+1):
        num = num * i
    print(num)

# 2.
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

N = int(input())
print(factorial(N))