# <4562>

'''
Zombies love to eat brains. Yum.

The first line contains a single integer n indicating the number of data sets.

The following n lines each represent a data set.
Each data set will be formatted according to the following description:

A single data set consists of a line "X Y",
where X is the number of brains the zombie eats and Y is the number of brains the zombie requires to stay alive.

For each data set, there will be exactly one line of output.
This line will be "MMM BRAINS" if the number of brains the zombie eats\
is greater than or equal to the number of brains the zombie requires to stay alive.
Otherwise, the line will be "NO BRAINS".
'''

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    if a < b :
        print("NO BRAINS")
    else:
        print("MMM BRAINS")