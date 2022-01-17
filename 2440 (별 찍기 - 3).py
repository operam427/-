# < 2440 > (별 찍기 - 3)

''''※ 문제
첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제

※ 입력
첫째 줄에 N이 주어진다.

※ 출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다. '''

n = int(input())
new_n = n+1

for i in range(1, new_n):
    print('*' * (new_n - i))

n = int(input())

for i in range(0, n):
    print('*' * (n - i))
