# 문제 링크 (주석) : https://www.acmicpc.net/problem/30008
# 간단한 문제 설명 : 준영이의 각 과목별 등수를 바탕으로 등급을 계산
# 해결 방법 설명 : 각 과목에서의 백분율을 계산하고, 이를 바탕으로 등급을 결정
# 시간/공간 복잡도 : O(K) (K는 과목의 수)

# 입력 처리
N, K = map(int, input().split())
G = list(map(int, input().split()))

# 등급 계산
grades = []
for g in G:
    P = (g * 100) // N
    if P <= 4:
        grades.append(1)
    elif P <= 11:
        grades.append(2)
    elif P <= 23:
        grades.append(3)
    elif P <= 40:
        grades.append(4)
    elif P <= 60:
        grades.append(5)
    elif P <= 77:
        grades.append(6)
    elif P <= 89:
        grades.append(7)
    elif P <= 96:
        grades.append(8)
    else:
        grades.append(9)

# 결과 출력
print(' '.join(map(str, grades)))