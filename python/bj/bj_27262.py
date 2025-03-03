# 문제 링크 (주석) : https://www.acmicpc.net/problem/27262
# 간단한 문제 설명 : 미샤가 자신의 집이 있는 n층에 도달하기 위해 엘리베이터를 타는 경우와 계단을 이용하는 경우의 시간을 계산
# 해결 방법 설명 : 엘리베이터가 1층으로 내려온 후 n층까지 올라가는 시간과 계단을 이용한 시간을 계산
# 시간/공간 복잡도 : O(1) (상수 시간과 공간이 소요됨)

# 입력 받기
n, k, a, b = map(int, input().split())

# 엘리베이터 시간 계산
elevator_time = (k - 1) * b + (n - 1) * b

# 계단 시간 계산
stairs_time = (n - 1) * a

# 결과 출력
print(elevator_time, stairs_time)