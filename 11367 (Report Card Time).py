# <11367>

'''
Little hobbitses go to hobbit school in the Shire.
They just finished a course, which involved tea-making,
meal-eating, nap-taking, and gardening. Based on the following grading scale,
assign each hobbit a letter grade based on their final numerical course grade.

A+: 97-100
A: 90-96
B+: 87-89
B: 80-86
C+: 77-79
C: 70-76
D+: 67-69
D: 60-66
F: 0-59

The input will begin with a single line containing just a whole number, n, of the number of hobbits in the class,
followed by n lines in the form a b, where a is the hobbit’s name (only alphabetical characters)
and b is the hobbit’s grade, given as a whole number. The length of hobbit's name is less than 10.

For each test case, print out a list of every hobbits name and letter grade,
each on its own line. There should be no additional white space following test cases.
'''

n = int(input())

for i in range(n):
    a, b = map(str, input().split())

    if 97 <= int(b) <= 100:
        print("{} {}".format(a, "A+"))
    elif 90 <= int(b) <= 96:
        print("{} {}".format(a, "A"))
    elif 87 <= int(b) <= 89:
        print("{} {}".format(a, "B+"))
    elif 80 <= int(b) <= 86:
        print("{} {}".format(a, "B"))
    elif 77 <= int(b) <= 79:
        print("{} {}".format(a, "C+"))
    elif 70 <= int(b) <= 76:
        print("{} {}".format(a, "C"))
    elif 67 <= int(b) <= 69:
        print("{} {}".format(a, "D+"))
    elif 60 <= int(b) <= 66:
        print("{} {}".format(a, "D"))
    elif 0 <= int(b) <= 59:
        print("{} {}".format(a, "F"))
