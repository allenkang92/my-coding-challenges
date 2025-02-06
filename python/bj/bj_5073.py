# 문제 링크 (주석) : https://www.acmicpc.net/problem/5073 
# 간단한 문제 설명 : 
#   세 변의 길이를 입력받아 삼각형의 종류를 판별하는 문제입니다.
#   - Equilateral: 세 변의 길이가 모두 같은 경우
#   - Isosceles: 두 변의 길이만 같은 경우
#   - Scalene: 세 변의 길이가 모두 다른 경우
#   - Invalid: 가장 긴 변의 길이가 다른 두 변의 길이의 합보다 크거나 같은 경우
#
# 해결 방법 설명 : 
#   - 세 변의 길이를 입력받아 정렬합니다.
#   - 삼각형 조건을 먼저 확인합니다. (가장 긴 변 < 다른 두 변의 합)
#   - 조건에 따라 삼각형의 종류를 판별하여 출력합니다.
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(1)
#   - 공간 복잡도: O(1)

while True:
    # 세 변의 길이 입력
    a, b, c = map(int, input().split())
    
    # 종료 조건 확인
    if a == b == c == 0:
        break
        
    # 길이순으로 정렬
    sides = sorted([a, b, c])
    
    # 삼각형 조건 확인 (가장 긴 변 < 다른 두 변의 합)
    if sides[2] >= sides[0] + sides[1]:
        print("Invalid")
    # 세 변이 모두 같은 경우
    elif a == b == c:
        print("Equilateral")
    # 두 변만 같은 경우
    elif a == b or b == c or a == c:
        print("Isosceles")
    # 세 변이 모두 다른 경우
    else:
        print("Scalene")