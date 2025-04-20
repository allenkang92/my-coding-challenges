# 문제 링크 : https://www.acmicpc.net/problem/10815
# 간단한 문제 설명 : N개의 숫자 카드를 가지고 있을 때, M개의 숫자들이 카드에 있는지 확인합니다.
# 해결 방법 설명 : 1. 카드 숫자들을 집합(set)으로 변환하여 검색 속도 향상
#                2. 각 찾을 숫자에 대해 카드 집합에 있는지 확인
# 시간/공간 복잡도 : O(M) (M은 찾을 숫자의 개수)

N = int(input())
card_num = set(map(int, input().split()))  # 집합으로 변환하여 검색 속도 향상
M = int(input())
find_num = list(map(int, input().split()))

# 각 숫자에 대해 결과 출력
result = []
for num in find_num:
    result.append('1' if num in card_num else '0')

print(' '.join(result))  # 공백으로 구분하여 출력