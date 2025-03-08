# 문제 링크 (주석) : https://www.acmicpc.net/problem/30585
# 간단한 문제 설명 : 
#   팝잇(Pop-it) 장난감에서 모든 돌기를 같은 상태로 만들기 위한 최소 전환 횟수 구하기
#   - 팝잇은 h x w 크기의 직사각형 모양
#   - 각 돌기는 0(튀어나온 상태) 또는 1(들어간 상태)로 표시됨
#   - 모든 돌기를 같은 상태(모두 0 또는 모두 1)로 만들어야 함
# 
# 해결 방법 설명 :
#   1. 현재 0과 1의 개수를 세어봄
#   2. 모든 돌기를 0으로 만드는 방법(1의 개수만큼 전환) 또는
#      모든 돌기를 1로 만드는 방법(0의 개수만큼 전환) 중 더 적은 것을 선택
#            
# 시간/공간 복잡도 : O(h * w) - 모든 돌기를 한 번씩 확인해야 함

# 입력 처리
h, w = map(int, input().split())

# 0과 1의 개수 세기
count_0 = 0
count_1 = 0

for _ in range(h):
    row = input()
    for state in row:
        if state == '0':
            count_0 += 1
        else:
            count_1 += 1

# 최소 전환 횟수 계산
min_switches = min(count_0, count_1)

# 결과 출력
print(min_switches)