# 문제 링크 (주석) : https://www.acmicpc.net/problem/32776
# 간단한 문제 설명 : 고속철도와 항공편의 소요 시간을 비교하여 어떤 교통수단을 더 많이 이용하는지 결정
# 해결 방법 설명 : 고속철도의 소요 시간과 항공편의 소요 시간을 비교하고, 고속철도의 소요 시간이 4시간 이하인지 확인
# 시간/공간 복잡도 : O(1)

# 고속철도의 소요 시간 입력
S_ab = int(input())

# 항공편의 소요 시간 입력 (M_a, F_ab, M_b)
M_a, F_ab, M_b = map(int, input().split())

# 항공편의 총 소요 시간 계산
flight_time = M_a + F_ab + M_b

# 고속철도를 더 많이 이용하는 조건 확인
if (S_ab <= flight_time) or (S_ab <= 240):
    print("high speed rail")
else:
    print("flight")