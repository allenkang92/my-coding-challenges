# 문제 링크 : https://www.acmicpc.net/problem/10699
# 간단한 문제 설명 : 서울의 오늘 날짜를 출력하는 프로그램을 작성하시오.
# 해결 방법 설명 : 

import datetime
now = datetime.datetime.now()

date = now.date()
print(date)
