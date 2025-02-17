# 문제 링크 (주석) : https://www.acmicpc.net/problem/6778
# 문제 설명:
#   목격자가 본 외계인의 안테나 수와 눈의 수를 입력받아,
#   아래 조건에 해당하는 외계인의 이름들을 출력하는 문제입니다.
#
# 외계인의 조건은 다음과 같습니다.
#   1) TroyMartian: 최소 3개의 더듬이와 최대 4개의 눈을 가짐.
#   2) 블라드사투르니안: 최대 6개의 더듬이와 적어도 2개의 눈을 가짐.
#   3) 그레임머큐리안: 최대 2개의 더듬이와 최대 3개의 눈을 가짐.
#
# 해결 방법 설명:
#   입력된 안테나 수(ant)와 눈의 수(eye)에 대해 각 조건을 체크하고,
#   조건에 맞는 외계인의 이름을 출력합니다.
#
# 시간/공간 복잡도 : O(1)

ant = int(input())
eye = int(input())

if ant >= 3 and eye <= 4:
    print("TroyMartian")
if ant <= 6 and eye >= 2:
    print("VladSaturnian")
if ant <= 2 and eye <= 3:
    print("GraemeMercurian")