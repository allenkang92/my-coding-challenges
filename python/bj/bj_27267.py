# 문제 링크 (주석) : https://www.acmicpc.net/problem/27267
# 문제 설명:
#   Masha와 Petya의 방 크기를 비교하는 문제입니다.
#   Masha의 방은 a x b (제곱미터) 크기이고, Petya의 방은 c x d (제곱미터) 크기입니다.
#   네 개의 자연수 a, b, c, d (1 ≤ a, b, c, d ≤ 1000)가 주어집니다.
#   Masha의 방이 더 크면 "M", Petya의 방이 더 크면 "P", 두 방의 면적이 같으면 "E"를 출력합니다.
#
# 해결 방법:
#   두 방의 면적을 각각 M = a * b, P = c * d로 계산한 후 비교합니다.
#
# 시간/공간 복잡도 : O(1)

a, b, c, d = map(int, input().split(" "))

M = a * b
P = c * d

if M > P:
    print("M")
elif M == P:
    print("E")
else:
    print("P")