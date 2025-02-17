# 문제 링크 (주석) : https://www.acmicpc.net/problem/6887
# 문제 설명:
#   Gigi는 정사각형 타일들을 모아서 테이블 위에 모두 배치해 내놓고자 한다.
#   사용 가능한 타일의 총 개수가 주어졌을 때, 만들 수 있는 가장 큰 정사각형의 한 변의 길이를 구하는 문제입니다.
#
# 해결 방법 설명:
#   주어진 N개의 타일로 만들 수 있는 가장 큰 정사각형의 한 변의 길이는 int(N ** 0.5)입니다.
#
# 시간/공간 복잡도 : O(1)

N = int(input())

print(f"The largest square has side length {int(N ** 0.5)}.")