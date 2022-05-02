# <1104>

'''
Eirik drinks a lot of Bingo Cola to help him program faster,\
and over the years he has burned many unnecessary calories walking all the way to the kitchen to get some.
To avoid this he has just bought a small fridge, which is beautifully placed next to his computer.
To make it match his fancy big-tower with all its blinking LEDs, it is necessary to style it a bit.

He has bought a weight sensor with a display and a small general purpose programmable chip,\
to put underneath the fridge.
The idea is to make the display show how many litres of Bingo Cola there is in the fridge.
To do this he must read a binary register in the sensor, and convert it to a decimal number to be displayed.

The first line of input gives n ≤ 1000, the number of test cases.
Then follow n lines with positive numbers represented as 24-bit binary strings (0s and 1s).

For each number, output its decimal representation, without any leading zeros.
'''

n = int(input())

for _ in range(n):
    number = input()
    num = 0
    for i in range(24):
        if number[i] == "1":
            num += 2 ** (23-i)
    print(num)
