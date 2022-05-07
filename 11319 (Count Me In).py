# <11319>

'''
Given a sentence in English, output the counts of consonants and vowels.
Vowels are letters in [’A’,’E’,’I’,’O’,’U’,’a’,’e’,’i’,’o’,’u’].

The test file starts with an integer S(1 ≤ S ≤ 100), the number of sentences.
Then follow S lines, each containing a sentence -words of length 1 to 20 separated by spaces.
Every sentence will contain at least one word and be comprised only of characters [a-z][A-Z] and spaces.
No sentence will be longer than 1000 characters.

For each sentence, output the number of consonants and vowels on a line, separated by space.
'''

S = int(input())

V = ["a", "e", "i", "o", "u"]
C = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

for _ in range(S):
    st = input().lower()

    num1 = 0
    num2 = 0

    for i in range(len(st)):
        if st[i] in V:
            num1 += 1
        elif st[i] in C:
            num2 += 1
    print("{} {}".format(num2, num1))
