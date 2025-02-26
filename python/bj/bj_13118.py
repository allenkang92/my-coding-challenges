# 문제 링크 (주석) : https://www.acmicpc.net/problem/13118
# 간단한 문제 설명 : 사과가 떨어질 때, 사과와 충돌하는 사람이 있는지를 확인하는 프로그램입니다.
# 해결 방법 설명 : 사람의 위치와 사과의 위치 및 반지름을 기반으로 충돌 여부를 판단합니다.
# 시간/공간 복잡도 : O(1)

# 사람들의 위치 입력
people_position = list(map(int, input().split(" ")))  # 사람들의 x축 위치

# 사과의 위치와 반지름 입력
x, y, r = map(int, input().split(" "))  # 사과의 중심과 반지름

# 사과의 x좌표가 사람들의 위치에 있는지 확인
if x in people_position:
    print(people_position.index(x) + 1)  # 충돌하는 사람의 번호 출력 (1부터 시작)
else:
    print(0)  # 충돌하는 사람이 없으면 0 출력