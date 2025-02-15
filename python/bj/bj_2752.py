# 문제 링크 (주석) : https://www.acmicpc.net/problem/2752
# 간단한 문제 설명 : 세 개의 정수를 오름차순으로 정렬하여 출력
# 해결 방법 설명 : 파이썬의 sorted 함수를 이용하여 리스트를 정렬한 후 언패킹하여 출력
# 시간/공간 복잡도 : O(1)

a, b, c = map(int, input().split(" "))

sort_list = sorted([a, b, c])

print(*sort_list)