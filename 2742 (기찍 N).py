# < 2742번 > (기찍 N)

# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

# 1. 옛날에 작성했던 코드. 사실 a = N + 1 - i  굳이 안 해도 되고, 바로 print(N + 1 - i) 해 버려도 된다.
N = int(input())

for i in range(1, N+1):
    a = N + 1 - i
    print(a)

# 2. 좀 더 깔끔한 코드
N = int(input())

for i in range(N, 0, -1):
    print(i)
