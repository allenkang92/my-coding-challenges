# 문제 링크 : https://www.acmicpc.net/problem/26767
# 문제 설명:
#   Bajtynka는 7과 11로 나누어 떨어지는 숫자에 특별한 외침을 합니다.
#   1부터 N까지의 숫자를 출력하는데,
#     - 숫자가 7로 나누어 떨어지면 "Hurra!"를 출력하며,
#     - 숫자가 11로 나누어 떨어지면 "Super!"를 출력하며,
#     - 숫자가 7과 11 모두로 나누어 떨어지면 "Wiwat!"를 출력합니다.
#   (각 숫자는 한 줄에 하나씩 출력합니다.)
#
# 해결 방법:
#   1부터 N까지 반복하면서, 해당 숫자가 7과 11으로 모두 나누어 떨어지면 "Wiwat!"
#   그렇지 않고 7로만 떨어지면 "Hurra!", 11로만 떨어지면 "Super!"를 출력하고,
#   그렇지 않으면 그냥 숫자를 출력합니다.
#
# 시간/공간 복잡도 : O(N)

N = int(input())

for i in range(1, N + 1):
    if i % 7 == 0 and i % 11 == 0:
        print("Wiwat!")
    elif i % 7 == 0:
        print("Hurra!")
    elif i % 11 == 0:
        print("Super!")
    else:
        print(i)