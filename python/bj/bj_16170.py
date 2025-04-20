# 문제 링크 : https://www.acmicpc.net/problem/16170
# 간단한 문제 설명 : 현재 시각을 UTC+0(세계 표준시)을 기준으로 나타냈을 때의 연도, 월, 일을 한 줄에 하나씩 순서대로 출력한다.
# 해결 방법 설명 : datetime 모듈을 사용하여 현재 UTC 시간을 구하고, strftime() 함수를 사용하여 연도, 월, 일을 각각 출력한다.
# 시간/공간 복잡도 : O(1)

import datetime

now_utc = datetime.datetime.utcnow()

print(now_utc.strftime("%Y"))
print(now_utc.strftime("%m"))
print(now_utc.strftime("%d"))