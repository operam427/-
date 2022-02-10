# <11653> 소인수분해

# 1
N = int(input())
num = 2

while N != 1:
    if N % num == 0:
      N = N // num
      print(num)
    else:
      num += 1

# 2
N = int(input())
num = 2

while N != 1 :
  if N % num == 0 :
    N = N // num
    print(num)
  else :
    num += 1
