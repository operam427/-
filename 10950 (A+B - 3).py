# < 10950번 >

''' 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다.

(0<A, B<10) '''

# 과거의 내 풀이

number = int(input())

for i in range(0, number):
    a, b = map(int, input().split())
    i = a + b

    print(i)

# 한 줄 줄일수 있는 풀이

number = int(input())

for i in range(0, number):
    a, b = map(int, input().split())

    print(a + b)

# 이런 풀이도 있다

number = int(input())
c = []
for i in range(number):
    a,b = map(int,input().split())
    c.append(a+b)
for i in range(number):
    print(c[i])
