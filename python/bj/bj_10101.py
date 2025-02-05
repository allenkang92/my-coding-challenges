# 문제 링크 (주석) : https://www.acmicpc.net/problem/10101
# 간단한 문제 설명 : 
#   삼각형의 세 각을 입력받아 삼각형의 종류를 판별하는 문제입니다.
#
# 해결 방법 설명 : 
#   1. 세 각의 합이 180이 아니면 Error
#   2. 세 각이 모두 60이면 Equilateral
#   3. 두 각이 같으면 Isosceles
#   4. 모든 각이 다르면 Scalene
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(1)
#   - 공간 복잡도: O(1)

angle_one = int(input())
angle_two = int(input())
angle_three = int(input())

angles = [angle_one, angle_two, angle_three]

if sum(angles) != 180:
    print("Error")
elif angle_one == angle_two == angle_three:
    print("Equilateral")
elif angle_one == angle_two or angle_two == angle_three or angle_one == angle_three:
    print("Isosceles")
else:
    print("Scalene")