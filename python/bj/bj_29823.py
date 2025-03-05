# 문제 링크 (주석) : https://www.acmicpc.net/problem/29823
# 간단한 문제 설명 : 로봇이 이동한 방향을 바탕으로, 시작점으로 돌아가기 위해 필요한 최소 이동 횟수를 계산
# 해결 방법 설명 : 각 방향으로의 이동 횟수를 계산하고, 상쇄된 이동 횟수의 합을 계산
# 시간/공간 복잡도 : O(N) (N은 이동 횟수)

# 입력 처리
N = int(input())
moves = input().strip()

# 이동 횟수 계산
north = moves.count('N')
south = moves.count('S')
east = moves.count('E')
west = moves.count('W')

# 남은 이동 횟수 계산
remaining_north_south = abs(north - south)
remaining_east_west = abs(east - west)

# 결과 출력
print(remaining_north_south + remaining_east_west)