# 문제 링크 : https://codeup.kr/problem.php?id=6068
# 간단한 문제 설명 :
#   점수(0~100)를 입력받아 평가를 출력하는 문제입니다.
#   90~100: A, 70~89: B, 40~69: C, 0~39: D
#
# 시간/공간 복잡도 : O(1)

n = int(input())

if n >= 90:
    print("A")
elif n >= 70:
    print("B")
elif n >= 40:
    print("C")
else:
    print("D")