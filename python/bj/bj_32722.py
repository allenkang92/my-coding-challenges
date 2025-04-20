# 문제 링크 : https://www.acmicpc.net/problem/32722
# 간단한 문제 설명 : Juta가 이동한 경로에서 만난 숫자들의 순서가 가능한지 확인
# 해결 방법 설명 : 왼쪽에서 오른쪽으로 이동하면서 만날 수 있는 숫자 조합 확인
# 시간/공간 복잡도 : O(1)

# 이미지에 표시된 육각형들의 숫자 배치
# 각 육각형에는 위아래로 숫자가 있음:
#  1   6   2
#  3   8   5

# 각 위치(열)의 가능한 숫자들
hexagons = [
    [1, 3],  # 첫 번째 육각형의 숫자들
    [6, 8],  # 두 번째 육각형의 숫자들
    [2, 5]   # 세 번째 육각형의 숫자들
]

# 입력 처리
try:
    # 한 줄에 세 개의 숫자가 주어지는 경우
    line = input().strip()
    if ' ' in line:
        first, second, third = map(int, line.split())
    else:
        first = int(line)
        second = int(input())
        third = int(input())
except:
    # 각 줄에 하나의 숫자가 주어지는 경우
    first = int(input())
    second = int(input())
    third = int(input())

# 세 숫자가 순서대로 나타날 수 있는지 확인
def can_appear_in_sequence(num1, num2, num3):
    # 각 숫자가 해당 위치의 육각형에 있는지 확인
    return (num1 in hexagons[0] and 
            num2 in hexagons[1] and 
            num3 in hexagons[2])

# 결과 출력
if can_appear_in_sequence(first, second, third):
    print("JAH")
else:
    print("EI")