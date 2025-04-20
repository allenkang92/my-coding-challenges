# 문제 링크 : https://www.acmicpc.net/problem/20233
# 간단한 문제 설명 : 두 가지 자전거 대여 옵션 중 어느 것이 더 경제적인지 계산하는 문제
# 해결 방법 설명 : 각 옵션의 월별 요금과 추가 요금을 고려하여 11월 동안의 총 비용을 계산
# 시간/공간 복잡도 : O(1) (입력 크기에 관계없이 일정한 시간과 공간이 소요됨)

# 입력 받기
a = int(input())  # 옵션 1의 월별 요금
x = int(input())  # 옵션 1의 추가 요금 (30분 초과 시)
b = int(input())  # 옵션 2의 월별 요금
y = int(input())  # 옵션 2의 추가 요금 (45분 초과 시)
T = int(input())  # 매일 사용하는 시간

# 옵션 1의 총 비용 계산
if T <= 30:
    option1 = a
else:
    option1 = a + (T - 30) * x * 21

# 옵션 2의 총 비용 계산
if T <= 45:
    option2 = b
else:
    option2 = b + (T - 45) * y * 21

# 결과 출력
print(option1, option2)