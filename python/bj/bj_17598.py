# 문제 링크 (주석) : https://www.acmicpc.net/problem/17598
# 문제 설명:
#   Animal Kingdom의 왕인 King Dragon이 세상을 떠난 후, Animal Kingdom의 새 왕을 선출해야 합니다.
#   총 9명의 유권자가 있으며, 후보는 Tiger와 Lion입니다.
#   9명의 투표 중 과반수(최소 5표)를 얻은 후보가 새 왕이 됩니다.
#
# 해결 방법 설명:
#   9줄에 걸쳐 각 투표(문자열)가 주어집니다.
#   각 후보의 득표수를 계산한 후, 5표 이상을 얻은 후보의 이름을 출력합니다.
#
# 시간/공간 복잡도 : O(1)

voted_list = []
for _ in range(9):
    voted_list.append(input())

if voted_list.count("Tiger") >= 5:
    print("Tiger")
elif voted_list.count("Lion") >= 5:
    print("Lion")