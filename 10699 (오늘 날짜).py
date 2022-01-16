# < 10699 >

# 서울의 오늘 날짜를 "YYYY-MM-DD" 형식으로 출력하는 프로그램을 작성하시오.

# 1. now 함수를 이용해 지금의 날짜, 시간을 출력
import datetime
print(str(datetime.datetime.now())[:10])

# 2. today 함수를 이용해 오늘의 날짜, 시간을 출력
import datetime
print(str(datetime.datetime.today())[:10])
