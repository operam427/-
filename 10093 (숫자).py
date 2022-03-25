# <10093>

'''
두 양의 정수가 주어졌을 때, 두 수 사이에 있는 정수를 모두 출력하는 프로그램을 작성하시오.
두 정수 A와 B가 주어진다.
첫째 줄에 두 수 사이에 있는 수의 개수를 출력한다.
둘째 줄에는 두 수 사이에 있는 수를 오름차순으로 출력한다.
'''

A, B = map(int, input().split())

NA = min(A, B)
NB = max(A, B)
num = []

for i in range(NA+1, NB):
    num.append(i)
print(len(num))

for v in range(len(num)):
    print(num[v], end=" ")

