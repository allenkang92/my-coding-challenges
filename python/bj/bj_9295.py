# 문제 링크 : https://www.acmicpc.net/problem/9295
# 문제 설명:
#   테스트 케이스의 개수 T와 각 테스트 케이스에서 주사위를 두 번 던져 나온 두 수가 주어집니다.
#   각 테스트 케이스마다 "Case x: "를 출력한 후 두 수의 합을 출력하는 문제입니다.
#
# 해결 방법 설명:
#   첫 줄에 테스트 케이스의 개수 T를 입력받고,
#   이후 각 테스트 케이스마다 두 수를 입력받아 합을 계산하고, 
#   "Case x: [합]" 형식으로 출력합니다.
#
# 시간/공간 복잡도 : O(T)

T = int(input())

for case in range(1, T + 1):
    dice_values = list(map(int, input().split()))
    sum_values = sum(dice_values)
    print(f"Case {case}: {sum_values}")