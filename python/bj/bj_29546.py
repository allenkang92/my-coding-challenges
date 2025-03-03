# 문제 링크 (주석) : https://www.acmicpc.net/problem/29546
# 간단한 문제 설명 : 사진 파일 이름과 선택된 구간이 주어졌을 때, 해당 구간에 속하는 파일 이름을 순서대로 출력
# 해결 방법 설명 : 각 구간에 해당하는 파일 이름을 순서대로 리스트에 추가하고 출력
# 시간/공간 복잡도 : O(n * m) (사진 파일 수와 구간 수에 비례하여 시간과 공간이 소요됨)

# 입력 받기
n = int(input())
files = [input().strip() for _ in range(n)]
m = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(m)]

# 결과 리스트 초기화
result = []

# 각 구간에 대해 처리
for l, r in intervals:
    result.extend(files[l-1:r])

# 결과 출력
for file in result:
    print(file)