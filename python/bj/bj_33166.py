# 문제 링크 (주석) : https://www.acmicpc.net/problem/33166
# 간단한 문제 설명 : 
#   JOI 철도의 운임을 계산하는 문제:
#   - 처음 P km까지는 1 km당 A엔
#   - P km 이후부터는 1 km당 B엔
#   - Q km 탑승할 때 총 운임 계산하기
# 
# 해결 방법 설명 :            
#   1. Q km가 P km 이하인 경우: Q * A
#   2. Q km가 P km보다 큰 경우: P * A + (Q - P) * B
# 
# 시간/공간 복잡도 : O(1) - 단순 계산만 수행함

# 입력 처리
P, Q = map(int, input().split())
A, B = map(int, input().split())

# 운임 계산
if Q <= P:
    # 전체 거리가 초기 요금 구간 내에 있는 경우
    fare = Q * A
else:
    # 초기 요금 구간과 추가 요금 구간으로 나눠서 계산
    fare = P * A + (Q - P) * B

# 결과 출력
print(fare)