# 문제 링크 : https://www.acmicpc.net/problem/33612
# 간단한 문제 설명 : 
#   피갤컵은 7개월 주기로 열리며, 1회는 2024년 8월, 2회는 2025년 3월에 열림
#   N번째 피갤컵이 열리는 연도와 월을 계산하는 문제
#
# 해결 방법 설명 :            
#   1. 1회 피갤컵(2024년 8월)을 기준으로 함
#   2. N번째 피갤컵은 기준에서 (N-1)*7개월 후에 열림
#   3. 월이 12를 초과하는 경우 연도를 적절히, 월은 1~12 범위로 조정
#
# 시간/공간 복잡도 : O(1) - 단순 계산만 수행

N = int(input())

year, month = 2024, 8

if N > 1:
    # (N-1)*7 개월을 더해야
    month += (N-1) * 7
    
    # 월이 12를 초과하는 경우 연도 조정
    year += (month - 1) // 12
    month = ((month - 1) % 12) + 1

print(year, month)