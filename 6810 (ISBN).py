# <6810>

'''
The International Standard Book Number (ISBN) is a 13-digit code for identifying books.
These numbers have a special property for detecting whether the number was written correctly.
The 1-3-sum of a 13-digit number is calculated by multiplying the digits alternately by 1’s and 3’s\
(see example) and then adding the results.

For example, to compute the 1-3-sum of the number 9780921418948 we add
9 ∗ 1 + 7 ∗ 3 + 8 ∗ 1 + 0 ∗ 3 + 9 ∗ 1 + 2 ∗ 3 + 1 ∗ 1 + 4 ∗ 3 + 1 ∗ 1 + 8 ∗ 3 + 9 ∗ 1 + 4 ∗ 3 + 8 ∗ 1 to get 120.

The special property of an ISBN number is that its 1-3-sum is always a multiple of 10.
Write a program to compute the 1-3-sum of a 13-digit number.
To reduce the amount of typing, you may assume that the first ten digits will always be 9780921418,
\like the example above.
Your program should input the last three digits and then print its 1-3-sum.
Use a format similar to the samples below.
'''

# 1
ISBN = [9, 7, 8, 0, 9, 2, 1, 4, 1, 8]

for i in range(3):
    ISBN.append(int(input()))

num = 0
count = 1

for a in ISBN:
    if count % 2 == 1:
        num += a * 1
    else:
        num += a * 3
    count += 1
print("The 1-3-sum is {}".format(num))

# 2

a1 = int(input())
b1 = int(input())
c1 = int(input())
print("The 1-3-sum is {0}".format(91+a1+c1+b1*3))