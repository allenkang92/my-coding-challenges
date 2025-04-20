# 문제 링크 : https://www.acmicpc.net/problem/10871
# 간단한 문제 설명 : 
#   정수 N개로 이루어진 수열 A와 정수 X가 주어짐
#   수열 A에서 X보다 작은 수를 모두 출력
#
# 해결 방법 설명 : 
#   - N과 X를 입력받음
#   - N개의 정수로 이루어진 수열 A를 입력받음
#   - A를 순회하며 X보다 작은 수를 찾아 출력
#   - else: pass는 불필요하므로 제거 가능
#   - sep=" "는 단일 값 출력시 불필요
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(N) - 수열 한 번 순회
#   - 공간 복잡도: O(N) - N개 정수 저장

N, X = map(int, input().split(" "))
A = list(map(int, input().split(" ")))

for i in A:
    if X > i:
        print(i, sep=" ", end=" ")
    else:
        pass