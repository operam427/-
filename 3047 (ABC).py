# <3047>

'''
세 수 A, B, C가 주어진다. A는 B보다 작고, B는 C보다 작다.
세 수 A, B, C가 주어졌을 때, 입력에서 주어진 순서대로 출력하는 프로그램을 작성하시오.

첫째 줄에 세 수 A, B, C가 주어진다.
하지만, 순서는 A, B, C가 아닐 수도 있다.
세 수는 100보다 작거나 같은 자연수이다.
둘째 줄에는 A, B, C로 이루어진 세 글자가 주어지며, 이 순서대로 출력하면 된다.

주어진 세 수를 주어진 출력 순서대로 출력하면 된다.
'''

a = list(map(int, input().split()))
a.sort()
A = a[0]
B = a[1]
C = a[2]

code = input()

if code == "ABC":
    print("{} {} {}".format(A,B,C))
elif code == "ACB":
    print("{} {} {}".format(A,C,B))
elif code == "BAC":
    print("{} {} {}".format(B,A,C))
elif code == "BCA":
    print("{} {} {}".format(B,C,A))
elif code == "CAB":
    print("{} {} {}".format(C,A,B))
elif code == "CBA":
    print("{} {} {}".format(C,B,A))
