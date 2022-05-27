# <18398>

'''
In one of the beautiful cities of Afghanistan two sisters are going to program a simple game\
to help them solve their mathematics homework.
Their homework asks them to calculate the sum and multiplication of two numbers.
Your task is to help them to build a simple program for their homework.

First line contains the number of test cases (T).

T test cases follow. For each test case, the first line represents the number of problems.
Next N lines contains two integer numbers Ai, Bi.

For every input expecting two integer numbers,\
first one represents the addition of two given numbers and second represents the multiplication separated by space.

'''

T = int(input())

for _ in range(T):
    N = int(input())
    for i in range(N):
        a, b = map(int, input().split())
        print("{} {}".format(a+b, a*b))