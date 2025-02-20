# 문제 링크 (주석) : https://www.acmicpc.net/problem/25991
# 문제 설명:
#   창고에 저장된 Boron Acetate Phosphoric Carbonate (BAPC) 액체를
#   하나의 큐브 모양 용기에 모두 담으려고 합니다.
#   현재 n개의 큐브 모양 용기에 BAPC가 들어있으며, 각각 한 변의 길이가 c입니다.
#   각 용기의 부피는 c^3 입니다.
#   모든 용기의 총 부피를 합한 후, 이를 딱 맞게 담아낼 수 있는 하나의 큐브 용기의 한 변의 길이를 구해야 합니다.
#
# 해결 방법:
#   각 용기의 부피를 계산하여 모두 더한 뒤, 그 총 부피의 세제곱근을 구하면 됩니다.
#
# 시간/공간 복잡도 : O(n)

n = int(input())
side_lengths = list(map(float, input().split()))

total_volume = sum(c**3 for c in side_lengths)
result = total_volume ** (1/3)

print(result)