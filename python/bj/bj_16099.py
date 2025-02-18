# 문제 링크 (주석) : https://www.acmicpc.net/problem/16099
# 문제 설명:
#   TelecomParisTech와 Eurecom 두 학교의 스포츠 시설 면적을 비교하는 문제입니다.
#   각 학교의 스포츠 필드 크기는 가로와 세로 길이로 주어지며,
#   TelecomParisTech의 경우 lt와 wt, Eurecom의 경우 le와 we가 주어집니다.
#   두 학교의 필드 면적을 계산하여, 면적이 더 큰 학교의 이름을 출력합니다.
#   만약 두 면적이 동일하면 "Tie"를 출력합니다.
#
# 해결 방법 설명:
#   각 학교의 면적은 (가로 × 세로)로 계산됩니다.
#   테스트 케이스마다 TelecomParisTech의 면적과 Eurecom의 면적을 계산한 후 비교합니다.
#
# 시간/공간 복잡도 : O(1) per 테스트 케이스

T = int(input())
for _ in range(T):
    lt, wt, le, we = map(int, input().split())
    TelecomParisTech = lt * wt
    Eurecom = le * we
    if Eurecom > TelecomParisTech:
        print("Eurecom")
    elif Eurecom < TelecomParisTech:
        print("TelecomParisTech")
    else:
        print("Tie")