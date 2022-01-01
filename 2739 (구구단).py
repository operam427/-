# < 2739번 >

# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오.
# 출력 형식에 맞춰서 출력하면 된다.

# 옛날에 풀었던 방법
N = int(input())

for i in range(1,10) :
    print(N,"*",i,"=",N * i)


# 요즘 이런 문제 푸는 방법, 이게 더 편하다
N = int(input())

for i in range(1,10) :
    print("{} * {} = {}".format(N,i,N * i))
