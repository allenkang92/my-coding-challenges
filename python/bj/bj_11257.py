# 문제 링크 (주석) : https://www.acmicpc.net/problem/11257
# 문제 설명:
#   IT Passport Examination에서는 총 100문제로 구성된 시험에서 세 개의 분야(Strategy 35%, Management 25%, Technology 40%)
#   에 대해서 각각 점수가 주어집니다.
#   합격 기준은 다음과 같습니다.
#     - 총점이 55점 이상이어야 하고,
#     - 각 분야에서 최소 30% 이상의 점수를 받아야 합니다.
#
#   각 분야별 최소 점수는 다음과 같습니다.
#     - Strategy: 35 * 0.3 = 10.5 → 정수 점수로는 11점 이상이어야 함.
#     - Management: 25 * 0.3 = 7.5 → 정수 점수로는 8점 이상이어야 함.
#     - Technology: 40 * 0.3 = 12.0 → 12점 이상이어야 함.
#
#   입력으로는 첫 줄에 응시자 수 N이 주어지고,
#   이후 N개의 줄에 걸쳐 각 응시자의 시험번호(8자리 정수)와 
#   Strategy, Management, Technology 분야의 점수가 순서대로 주어집니다.
#
# 출력:
#   각 응시자마다 시험번호, 총점, 그리고 "PASS" 또는 "FAIL"을 출력합니다.
#   출력 순서는 입력 순서를 유지합니다.
#
# 해결 방법 설명:
#   각 응시자의 점수 S, I, T를 읽어 총점을 계산한 후,
#   총점이 55점 이상이고 각 분야 점수가 (35, 25, 40)의 30% 이상인지를 판단하여 합격 여부를 결정합니다.
#
# 시간/공간 복잡도 : O(1) per 응시자

N = int(input())

for _ in range(N):
    parti_num, S, I, T = input().split()
    S, I, T = int(S), int(I), int(T)
    total = S + I + T
    # 각 분야의 최소 통과 점수는 35*0.3, 25*0.3, 40*0.3 이며, 정수 점수이므로 (S, I, T)는 각각
    # S >= 10.5, I >= 7.5, T >= 12 이어야 하고, 정수 조건 상 S>=11, I>=8, T>=12로 판단할 수 있음.
    if total >= 55 and S >= 35 * 0.3 and I >= 25 * 0.3 and T >= 40 * 0.3:
        print(f"{parti_num} {total} PASS")
    else:
        print(f"{parti_num} {total} FAIL")