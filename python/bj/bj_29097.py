# 문제 링크 : https://www.acmicpc.net/problem/29097
# 간단한 문제 설명 : 세 명의 왕의 군대 규모를 비교하고, 가장 강력한 군대를 가진 왕의 이름을 출력
# 해결 방법 설명 : 각 왕의 군대 규모를 계산하고, 가장 큰 규모를 가진 왕의 이름을 출력
# 시간/공간 복잡도 : O(1) (상수 시간과 공간이 소요됨)

# 입력 받기
n, m, k, a, b, c = map(int, input().split())

# 각 왕의 군대 규모 계산
joffrey = n * a
robb = m * b
stannis = k * c

# 가장 큰 군대 규모 찾기
max_army = max(joffrey, robb, stannis)

# 결과 리스트 초기화
result = []

# 가장 큰 군대 규모를 가진 왕의 이름 추가
if joffrey == max_army:
    result.append("Joffrey")
if robb == max_army:
    result.append("Robb")
if stannis == max_army:
    result.append("Stannis")

# 결과 출력
print(' '.join(result))