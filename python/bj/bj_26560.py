# 문제 링크 : https://www.acmicpc.net/problem/26560
# 문제 설명:
#   Eric은 집중력이 부족해서 문장의 끝에 마침표를 찍는 것을 잊어버립니다.
#   Eric의 문장이 마침표로 끝나지 않으면, 문장의 끝에 마침표를 추가해 출력하는 프로그램을 작성하세요.
#
# 입력:
#   첫 번째 줄에는 입력될 문장의 수 n이 주어집니다.
#   이후 n개의 줄에 걸쳐 문장이 주어집니다.
#
# 출력:
#   각 문장을 출력할 때, 반드시 마지막에 마침표(.)가 있도록 출력합니다.
#
# 해결 방법:
#   각 줄을 입력받고, 만약 문장이 마침표로 끝나지 않으면 끝에 마침표를 추가하여 출력합니다.
#
# 시간/공간 복잡도 : O(n)

n = int(input())
for _ in range(n):
    sentence = input()
    if sentence.endswith("."):
        print(sentence)
    else:
        print(sentence + ".")