# 문제 링크 : https://www.acmicpc.net/problem/10817
# 간단한 문제 설명 : 세 정수 A, B, C가 주어질 때 두 번째로 큰 정수를 출력하는 문제
# 해결 방법 설명 : 세 개의 정수를 정렬한 후 가운데 값(인덱스 1)을 출력
# 시간/공간 복잡도 : O(1) - 항상 3개의 정수만 다루므로 상수 시간 복잡도

# 세 정수 입력 받기
A, B, C = map(int, input().split())

# 세 수를 리스트에 저장
ABC_list = [A, B, C]

# 리스트를 오름차순으로 정렬
ABC_list = sorted(ABC_list)

# 두 번째로 큰 정수(인덱스 1) 출력
print(ABC_list[1])