# 문제 링크 : https://www.acmicpc.net/problem/21875
# 간단한 문제 설명 : 체스판에서 Innohorse의 이동 유형을 결정
# 해결 방법 설명 : 시작 셀과 도착 셀의 좌표 차이를 계산하고, Innohorse의 이동 패턴을 만족하는 (x, y)를 찾음
# 시간/공간 복잡도 : O(1)

# 셀을 좌표로 변환하는 함수
def cell_to_coords(cell):
    x = ord(cell[0]) - ord('a')
    y = int(cell[1]) - 1
    return (x, y)

# 입력 처리
A = input().strip()
B = input().strip()

# 셀을 좌표로 변환
x1, y1 = cell_to_coords(A)
x2, y2 = cell_to_coords(B)

# 이동 거리 계산
dx = abs(x2 - x1)
dy = abs(y2 - y1)

# Innohorse의 이동 유형 결정
if dx > dy:
    x, y = dy, dx
else:
    x, y = dx, dy

# 결과 출력
print(x, y)