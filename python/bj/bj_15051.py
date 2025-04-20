# 문제 링크 : https://www.acmicpc.net/problem/15051
# 간단한 문제 설명 : 커피 머신을 어느 층에 설치해야 직원들의 총 이동 시간을 최소화할 수 있는지 계산하세요.
# 해결 방법 설명 : 커피 머신을 각 층에 설치했을 때의 총 이동 시간을 계산하고, 가장 작은 값을 선택합니다.
# 시간/공간 복잡도 : O(1)

# 각 층의 직원 수 입력 받기
A1 = int(input())  # 1층 직원 수
A2 = int(input())  # 2층 직원 수
A3 = int(input())  # 3층 직원 수

# 커피 머신을 각 층에 설치했을 때의 총 이동 시간 계산
time_floor1 = A2 * 2 + A3 * 4  # 1층에 설치
time_floor2 = A1 * 2 + A3 * 2  # 2층에 설치
time_floor3 = A1 * 4 + A2 * 2  # 3층에 설치

# 최소 이동 시간 선택
min_time = min(time_floor1, time_floor2, time_floor3)

# 결과 출력
print(min_time)