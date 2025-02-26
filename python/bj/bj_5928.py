# 문제 링크 (주석) : https://www.acmicpc.net/problem/5928
# 간단한 문제 설명 : 베시가 경진대회에 소요한 총 시간을 분 단위로 계산하는 문제입니다.
# 해결 방법 설명 : 시작 시간을 기준으로 끝낸 시간을 분 단위로 변환하여 차이를 계산합니다.
# 시간/공간 복잡도 : O(1)

D, H, M = map(int, input().split(" "))

# 시작 시간: 11월 11일 11시 11분
start_day = 11
start_hour = 11
start_minute = 11

# 끝낸 시간을 분 단위로 변환
end_total_minutes = (D - start_day) * 24 * 60 + (H - start_hour) * 60 + (M - start_minute)

# 끝낸 시간이 시작 시간보다 이전인 경우 -1 반환
if end_total_minutes < 0:
    print(-1)
else:
    print(end_total_minutes)
