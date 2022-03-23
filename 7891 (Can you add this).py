# <7891>

'''
Given two integers, calculate and output their sum.
The input contains several test cases.
The first line contains and integer t (t ≤ 100) denoting the number of test cases.
Then t tests follow, each of them consisiting of two space separated integers x and y (−109 ≤ x, y ≤ 109).

For each test case output output the sum of the corresponding integers.
'''

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    print(a+b)