# 문제 링크 : https://www.acmicpc.net/problem/26532
# 문제 설명:
#   옥수수 씨앗 한 봉지는 5 에이커를 덮을 수 있으며,
#   1 에이커는 4840 제곱야드입니다.
#   주어진 직사각형 밭의 가로(r1)와 세로(r2) 길이(야드)를 입력받아,
#   밭 전체를 심기 위해 필요한 옥수수 씨앗 봉지의 수를 계산합니다.
#
# 해결 방법:
#   1. 밭의 면적(제곱야드)을 계산합니다. (yard_square = r1 * r2)
#   2. 밭의 면적을 에이커로 변환합니다. (to_acres = yard_square / 4840)
#   3. 필요한 봉지 수는 (to_acres / 5)를 올림한 값입니다.
#      math 모듈을 사용하지 않고, if 조건문을 이용하여 처리할 수 있습니다.
#
# 시간/공간 복잡도 : O(1)

r1, r2 = map(float, input().split(" "))
yard_square = r1 * r2
to_acres = yard_square / 4840

# to_acres를 5로 나눈 값이 딱 떨어지면 그대로, 
# 아니라면 올림 (정수 나누기이므로 // 를 사용)
if to_acres % 5 == 0:
    print(int(to_acres // 5))
else:
    print(int((to_acres // 5) + 1))