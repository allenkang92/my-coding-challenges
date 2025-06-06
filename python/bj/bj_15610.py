# 문제 링크: https://www.acmicpc.net/problem/15610
# 문제 설명:
#   Bath Abbey의 정사각형 마당의 면적(a)이 주어지면, 마당의 네 변에 설치할
#   전기 배선의 총 길이를 구하는 문제입니다.
#   마당은 정사각형이므로 한 변의 길이는 √a이며, 전체 둘레는 4 × √a 입니다.
#
# 해결 방법 설명:
#   입력된 면적 a에 대해, 한 변의 길이를 a ** 0.5 로 계산한 후 4를 곱합니다.
#   math 모듈을 사용하지 않고도 거듭제곱 연산자를 이용하여 제곱근을 구할 수 있습니다.
#
# 시간/공간 복잡도 : O(1)

square = int(input())
m = square ** 0.5  # a의 제곱근 (√a) 계산
print(m * 4)       # 4 × √a 출력