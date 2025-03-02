# 문제 링크 (주석) : https://www.acmicpc.net/problem/24356
# 간단한 문제 설명 : 시작 시간과 종료 시간 사이의 경과 시간을 분 단위로 계산하고, 완주한 완전한 호수 주변의 횟수를 계산
# 해결 방법 설명 : 시작 시간과 종료 시간을 분 단위로 변환하여 경과 시간을 계산하고, 30분 단위로 완주 횟수를 계산
# 시간/공간 복잡도 : O(1) (입력 크기에 관계없이 일정한 시간과 공간이 소요됨)

# 입력 받기 (한 줄로 입력)
t1, m1, t2, m2 = map(int, input().split())

# 시작 시간과 종료 시간을 분 단위로 변환
start_time = t1 * 60 + m1
end_time = t2 * 60 + m2

# 종료 시간이 시작 시간보다 작으면 24시간(1440분)을 더함
if end_time < start_time:
    end_time += 1440

# 경과 시간 계산
elapsed_time = end_time - start_time

# 완주 횟수 계산 (30분 단위)
num_laps = elapsed_time // 30

# 결과 출력
print(elapsed_time, num_laps)