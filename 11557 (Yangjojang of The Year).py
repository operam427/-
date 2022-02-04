# 11557 (Yangjojang of The Year)

'''
입학 OT때 누구보다도 남다르게 놀았던 당신은 자연스럽게 1학년 과대를 역임하게 되었다.
타교와의 조인트 엠티를 기획하려는 당신은 근처에 있는 학교 중 어느 학교가 술을 가장 많이 먹는지 궁금해졌다.
학교별로 한 해동안 술 소비량이 주어질 때, 가장 술 소비가 많은 학교 이름을 출력하여라.

입력의 첫 줄에는 테스트 케이스의 숫자 T가 주어진다.
매 입력의 첫 줄에는 학교의 숫자 정수 N이 주어진다.
이어서 N줄에 걸쳐 학교 이름 S와 해당 학교가 지난 한 해동안 소비한 술의 양 L이 공백으로 구분되어 정수로 주어진다.
같은 테스트 케이스 안에서 소비한 술의 양이 같은 학교는 없다고 가정한다.

각 테스트 케이스마다 한 줄에 걸쳐 술 소비가 가장 많은 학교의 이름을 출력한다.
'''

import operator

dict = {}

T = int(input())

for _ in range(T):
    N = int(input())

    for _ in range(N):
        school, num = map(str, input().split())
        dict[school] = int(num)

    highest = max(dict.items(), key=operator.itemgetter(1))[0]
    print(highest)

    dict = {}
