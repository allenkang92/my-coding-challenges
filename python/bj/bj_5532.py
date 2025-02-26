# 문제 링크 (주석) : https://www.acmicpc.net/problem/5532
# 문제 설명:
#   상근이는 방학 동안 국어와 수학 숙제를 해야 한다.
#   방학은 총 L일이며, 국어는 총 A페이지, 수학은 총 B페이지를 풀어야 한다.
#   상근이는 하루에 국어를 최대 C페이지, 수학을 최대 D페이지 풀 수 있다.
#   숙제를 모두 마친 후 남은 방학 날 수를 구하는 문제이다.
#
# 해결 방법:
#   국어와 수학의 숙제를 각각 목표 페이지 수와 하루 최대 풀이 페이지 수로 나누어,
#   숙제를 마치는데 필요한 날짜를 계산한다.
#   만약 나누어떨어지지 않으면 올림 처리를 해준다.
#   두 과목 중 더 오래 걸리는 과목의 날짜가 숙제를 끝내는데 필요한 총 날짜이므로,
#   방학 일수 L에서 그 날짜를 빼면 상근이가 놀 수 있는 최대 날이 된다.
#
# 시간/공간 복잡도: O(1)

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

# 수학과 국어 숙제를 마치는데 필요한 날짜 계산 (올림 처리)
math_days = B // D
korean_days = A // C

if B % D > 0:
    math_days += 1
if A % C > 0:
    korean_days += 1

# 두 과목 중 더 많이 걸리는 날짜
required_days = max(math_days, korean_days)

# 남는 날 수 계산
print(L - required_days)