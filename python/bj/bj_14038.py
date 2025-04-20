# 문제 링크 : https://www.acmicpc.net/problem/14038
# 문제 설명:
#   한 대회에서 각 선수는 6게임을 진행하며, 무승부는 없습니다.
#   게임 결과에 따라 선수를 다음 그룹으로 배정합니다:
#     - 5승 이상: Group 1 (출력 1)
#     - 3승 또는 4승: Group 2 (출력 2)
#     - 1승 또는 2승: Group 3 (출력 3)
#     - 0승: 탈락 (출력 -1)
#
# 해결 방법 설명:
#   6줄에 걸쳐 입력되는 게임 결과(W 또는 L)를 리스트에 저장한 후,
#   리스트의 count 함수를 사용하여 "W"의 개수를 셉니다.
#   그 개수에 따라 적절한 그룹 번호 또는 탈락(-1)을 출력합니다.
#
# 시간/공간 복잡도 : O(1)

game1 = input()
game2 = input()
game3 = input()
game4 = input()
game5 = input()
game6 = input()

WL_list = [game1, game2, game3, game4, game5, game6]

wins = WL_list.count("W")

if wins >= 5:
    print(1)
elif wins >= 3:
    print(2)
elif wins >= 1:
    print(3)
else:
    print(-1)