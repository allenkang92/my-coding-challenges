# 문제 링크 : https://www.acmicpc.net/problem/5575
# 문제 설명:
#   JOI 상사의 3명의 직원 A, B, C의 출근 시간과 퇴근 시간이 주어졌을 때,
#   각 직원의 근무시간(시, 분, 초)을 계산하여 출력하는 문제입니다.
#
# 해결 방법 설명:
#   각 직원의 출근 시간을 초 단위로, 퇴근 시간을 초 단위로 변환한 후,
#   두 시간의 차이를 계산합니다.
#   이후 그 차이를 다시 시, 분, 초로 변환하여 출력합니다.
#
# 시간/공간 복잡도 : O(1)

def calc_work_time(time_info):
    # time_info: [출근시, 출근분, 출근초, 퇴근시, 퇴근분, 퇴근초]
    start_seconds = time_info[0] * 3600 + time_info[1] * 60 + time_info[2]
    end_seconds = time_info[3] * 3600 + time_info[4] * 60 + time_info[5]
    diff = end_seconds - start_seconds
    h = diff // 3600
    diff %= 3600
    m = diff // 60
    s = diff % 60
    return h, m, s

line_A = list(map(int, input().split()))
line_B = list(map(int, input().split()))
line_C = list(map(int, input().split()))

h_A, m_A, s_A = calc_work_time(line_A)
h_B, m_B, s_B = calc_work_time(line_B)
h_C, m_C, s_C = calc_work_time(line_C)

print(h_A, m_A, s_A)
print(h_B, m_B, s_B)
print(h_C, m_C, s_C)