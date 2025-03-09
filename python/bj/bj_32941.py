# 문제 링크 (주석) : https://www.acmicpc.net/problem/32941
# 간단한 문제 설명 : 
#   건우가 X교시에 교실을 예약했을 때, 모든 조원이 참석 가능한지 확인하는 문제
#   각 조원은 참석 가능한 교시 목록을 제공함
# 
# 해결 방법 설명 :            
#   1. 각 조원이 참석 가능한 교시 목록을 확인
#   2. 모든 조원이 X교시에 참석 가능한지 확인
#   3. 한 명이라도 X교시에 참석할 수 없으면 "NO", 모두 참석 가능하면 "YES" 출력
# 
# 시간/공간 복잡도 : O(N) - N은 조원의 수

# 입력 처리
T, X = map(int, input().split())
N = int(input())  # 조원의 수

all_can_attend = True  # 모든 조원이 참석 가능한지 여부

for _ in range(N):
    K = int(input())  # 조원이 참석 가능한 교시의 수
    available_times = list(map(int, input().split()))  # 참석 가능한 교시 목록
    
    # 이 조원이 X교시에 참석 가능한지 확인
    if X not in available_times:
        all_can_attend = False
        break

# 결과 출력
if all_can_attend:
    print("YES")
else:
    print("NO")