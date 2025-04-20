# 문제 링크 : https://www.acmicpc.net/problem/29267
# 간단한 문제 설명 : 게임에서의 다양한 동작(탄약 획득, 저장, 불러오기, 발사)을 처리하고, 각 동작 후의 탄약 수를 출력
# 해결 방법 설명 : 각 동작에 따라 탄약 수를 업데이트하고, 각 동작 후의 탄약 수를 출력
# 시간/공간 복잡도 : O(n) (동작 수에 비례하여 시간과 공간이 소요됨)

# 입력 받기
n, k = map(int, input().split())
actions = [input().strip() for _ in range(n)]

# 초기 탄약 수와 마지막 저장된 탄약 수 초기화
ammo = 0
last_save = 0

# 각 동작 처리
for action in actions:
    if action == "ammo":
        ammo += k
    elif action == "save":
        last_save = ammo
    elif action == "load":
        ammo = last_save
    elif action == "shoot":
        ammo -= 1
    # 결과 출력
    print(ammo)