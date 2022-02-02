# 3009

''' 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

직사각형의 네 번째 점의 좌표를 출력한다. '''

a1, a2 = map(int,input().split())
b1, b2 = map(int,input().split())
c1, c2 = map(int,input().split())

if a1 == b1:
    d1 = c1
elif a1 == c1:
    d1 = b1
else:
    d1 = a1

if a2 == b2:
    d2 = c2
elif a2 == c2 :
    d2 = b2
else :
    d2 = a2

print(d1, d2, end=" ")
