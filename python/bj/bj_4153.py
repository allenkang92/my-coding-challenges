# 문제 링크 (주석) : https://www.acmicpc.net/problem/4153
# 문제 설명:
#   주어진 세 변의 길이가 직각 삼각형을 이루는지 여부를 판별하는 문제이다.
#   직각 삼각형의 조건은 가장 긴 변의 제곱이 다른 두 변의 제곱의 합과 같아야 한다.
#
# 입력:
#   여러 테스트 케이스가 주어지며, 각 테스트 케이스는 세 변의 길이를 나타내는 양의 정수이다.
#   마지막 줄에는 "0 0 0"이 입력된다.
#
# 출력:
#   각 테스트 케이스마다 직각 삼각형이면 "right"를, 그렇지 않으면 "wrong"을 출력한다.
#
# 해결 방법:
#   각 테스트 케이스에서 입력받은 세 변의 길이를 정렬한 후,
#   가장 긴 변의 제곱이 나머지 두 변의 제곱의 합과 동일한지 확인한다.
#
# 시간/공간 복잡도: O(1) per test case

while True:
    side_list = sorted(list(map(int, input().split())))
    if side_list[0] == 0 and side_list[1] == 0 and side_list[2] == 0:
        break
    if side_list[2]**2 == side_list[0]**2 + side_list[1]**2:
        print("right")
    else:
        print("wrong")