# 문제 링크 (주석) : https://www.acmicpc.net/problem/30319
# 간단한 문제 설명 : 
#   ICPC Taoyuan Regional Contest는 2023년 10월 21일부터 10월 23일까지 개최
#   TOPC(Taiwan Online Programming Contest) 날짜는 Regional Contest보다 최소 35일 전이어야 함
#   주어진 날짜가 TOPC 개최에 너무 늦은지 판단하는 문제
#
# 해결 방법 설명 :            
#   1. ICPC Taoyuan Regional Contest 시작일(2023-10-21)에서 35일을 뺀 날짜 계산
#   2. 입력받은 TOPC 예상 개최일이 그 날짜보다 늦으면 "TOO LATE", 그렇지 않으면 "GOOD" 출력
#
# 시간/공간 복잡도 : O(1) - 단순 날짜 비교 연산만 수행

from datetime import datetime

# ICPC Taoyuan Regional Contest 시작일
regional_start = datetime(2023, 10, 21)

# 입력받은 TOPC 예상 개최일
topc_date_str = input()
topc_date = datetime.strptime(topc_date_str, "%Y-%m-%d")

# 35일 전 계산 (timedelta를 사용하지 않고 날짜 직접 비교)
# 2023-10-21에서 35일을 빼면 2023-09-16
deadline = datetime(2023, 9, 16)

# 결과 출력
if topc_date <= deadline:
    print("GOOD")
else:
    print("TOO LATE")