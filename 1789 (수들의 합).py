# <1789>

'''
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?
첫째 줄에 자연수 S가 주어진다.
첫째 줄에 자연수 N의 최댓값을 출력한다.
'''

# 1
S = int(input())
num = 0

for i in range(1,S+1):
    num += i
    if num > S:
        print(i-1)
        break

# 2
S = int(input())
num = 0
x = 0

for i in range(1,S+1):
    num += 1
    x += i
    if x > S:
        print(num-1)
        break


