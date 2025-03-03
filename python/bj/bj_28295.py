# 문제 링크 (주석) : https://www.acmicpc.net/problem/28295
# 간단한 문제 설명 : 학생들이 초기에 북쪽을 바라보고 있다가 10번의 지시에 따라 방향을 바꾸고, 최종적으로 바라보는 방향을 출력
# 해결 방법 설명 : 각 지시에 따라 학생들의 방향을 업데이트하고, 최종 방향을 출력
# 시간/공간 복잡도 : O(1) (상수 시간과 공간이 소요됨)

# 초기 방향 설정 (북쪽)
direction = 'N'

# 방향 회전을 위한 리스트 (북, 동, 남, 서)
directions = ['N', 'E', 'S', 'W']

# 10번의 지시 처리
for _ in range(10):
    t = int(input())
    if t == 1:  # 우향우 (오른쪽으로 90도 회전)
        direction = directions[(directions.index(direction) + 1) % 4]
    elif t == 2:  # 뒤로 돌아 (오른쪽으로 180도 회전)
        direction = directions[(directions.index(direction) + 2) % 4]
    elif t == 3:  # 좌향좌 (왼쪽으로 90도 회전)
        direction = directions[(directions.index(direction) - 1) % 4]

# 결과 출력
print(direction)