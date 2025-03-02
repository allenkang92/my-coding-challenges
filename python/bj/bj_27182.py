# 문제 링크: https://www.acmicpc.net/problem/27182
# 문제 설명: 현재 날짜(n)와 2주 전 일요일의 날짜(m)가 주어졌을 때, 지난 주 일요일의 날짜를 계산
# 해결 방법 설명 :            
# 시간/공간 복잡도 : 

# 입력 받기
n, m = map(int, input().split())

# 이 문제의 핵심은 지난 주 일요일이 m+7이라는 점입니다.
# 다만, 월이 바뀌었을 경우 추가 처리가 필요합니다.

# 지난 주 일요일 = 2주 전 일요일 + 7
last_sunday = m + 7

# 문제에서의 모든 달은 최소 28일이 있다고 가정
# 만약 last_sunday가 28을 초과하면, 월이 바뀐 것으로 간주
if last_sunday > 28:
    last_sunday = last_sunday - 28

print(last_sunday)
