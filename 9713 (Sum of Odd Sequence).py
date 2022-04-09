# <9713>

'''
Given an odd integer N, calculate the sum of all the odd integers between 1 and N inclusive.
First line of the input contains T, the number of test cases.

Each test case contains a single integer N. N is between 1 and 100.

For each test case output the value 1+3+….+N.
'''

T = int(input())

for _ in range(T):
    a = 0
    for i in range(0, int(input())+1):
        if i % 2 != 0:
            a += i
    print(a)
