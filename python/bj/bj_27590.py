# 문제 링크 : https://www.acmicpc.net/problem/27590
# 간단한 문제 설명 : 태양과 달이 특정 위치에 정렬되어 일식이 일어나는 시점을 계산
# 해결 방법 설명 : 태양과 달이 동시에 정렬되는 시점을 계산하고, 다음 일식이 일어나는 시점까지의 년수를 출력
# 시간/공간 복잡도 : O(5000) (최대 5000년까지 탐색하므로 상수 시간과 공간이 소요됨)

# 입력 받기
ds, ys = map(int, input().split())
dm, ym = map(int, input().split())

# 다음 일식이 일어나는 시점까지의 년수 계산
for year in range(1, 5001):
    if (year + ds) % ys == 0 and (year + dm) % ym == 0:
        print(year)
        break