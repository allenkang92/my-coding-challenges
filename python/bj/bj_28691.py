# 문제 링크 (주석) : https://www.acmicpc.net/problem/28691
# 간단한 문제 설명 :
#   민재가 동아리의 첫 번째 글자 하나를 이야기하면, 그 글자에 해당하는 동아리의 전체 이름을 출력하는 문제입니다.
#
# 해결 방법 설명 :
#   입력된 한 글자에 따라 조건문(if/elif)을 사용하여 대응하는 동아리의 전체 이름을 출력합니다.
#
# 시간/공간 복잡도 : O(1)

Capital = input()  # 민재가 이야기한 동아리의 첫 번째 글자 입력 (M, W, C, A, $ 중 하나)

if Capital == "M":
    print("MatKor")  # 정보보호학부 소속 동아리 MatKor 출력

elif Capital == "W":
    print("WiCys")   # 정보보호학부 소속 동아리 WiCys 출력

elif Capital == "C":
    print("CyKor")   # 사이버국방학과 소속 동아리 CyKor 출력

elif Capital == "A":
    print("AlKor")   # 사이버국방학과 소속 동아리 AlKor 출력

elif Capital == "$":
    print("$clear")  # 스마트보안학과 소속 동아리 $clear 출력