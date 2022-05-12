# <1676>

'''
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
첫째 줄에 N이 주어진다.
첫째 줄에 구한 0의 개수를 출력한다.
'''
import math
N = int(input())

a = str(math.factorial(N))
b = a[::-1]
count = 0

for i in range(len(b)):
    if b[i] == '0':
        count += 1
    else:
        break

print(count)