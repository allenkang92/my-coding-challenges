# 문제 링크 (주석) : https://www.acmicpc.net/problem/28249
# 문제 설명:
#   Ron은 다양한 종류의 고추를 사용하여 칠리를 만들고 있습니다.
#   각 고추의 매운 정도는 Scoville Heat Units (SHU)로 측정됩니다.
#   Ron의 칠리에 고추를 추가할 때마다 칠리의 총 매운 정도는 해당 고추의 SHU 값만큼 증가합니다.
#   아래 표는 사용 가능한 고추와 그에 해당하는 SHU 값을 보여줍니다.
#
#   고추 이름     : SHU 값
#   Poblano      : 1500
#   Mirasol      : 6000
#   Serrano      : 15500
#   Cayenne      : 40000
#   Thai         : 75000
#   Habanero     : 125000
#
#   입력:
#     첫 번째 줄에 Ron이 칠리에 추가한 고추의 개수 N이 주어집니다.
#     이후 N개의 줄에 걸쳐 추가된 각 고추의 이름이 주어집니다.
#
#   출력:
#     Ron의 칠리의 총 매운 정도(Total Spiciness)를 정수로 출력합니다.
#
# 해결 방법:
#   고추 이름과 SHU 값을 딕셔너리에 저장하고, 입력받은 고추 이름에 해당하는 SHU 값을 모두 합산하여 출력합니다.
#
# 시간/공간 복잡도: O(N)

N = int(input())

pepper_dict = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000
}

total_spiciness = 0

for _ in range(N):
    pepper = input()
    total_spiciness += pepper_dict[pepper]

print(total_spiciness)