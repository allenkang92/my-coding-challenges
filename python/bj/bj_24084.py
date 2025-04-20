# 문제 링크 : https://www.acmicpc.net/problem/24084
# 간단한 문제 설명: 
#   길이 N의 문자열 S가 주어지며, 각 문자는 J, O, I 중 하나이다.
#   비타로는 N-1번의 동작을 수행한다.
#   i번째 동작(1 ≤ i ≤ N-1)에서는 다음과 같이 행동한다:
#   S의 i+1번째 문자를 확인한다.
#   만약 S의 i+1번째 문자가 J라면, S의 i번째 문자를 칠판에 쓴다.
#   비타로가 칠판에 쓴 모든 문자를 순서대로 출력하는 문제이다.
#
# 해결 방법 설명:
#   문자열 S를 순회하면서, i+1번째 문자(즉, S[i+1])가 J인지 확인한다.
#   J라면 i번째 문자(S[i])를 결과 리스트에 추가하고, 마지막에 모든 결과를 출력한다.
#            
# 시간/공간 복잡도: O(N), N은 문자열의 길이

N = int(input())
S = input()

result = []

for i in range(N-1):
    if S[i+1] == 'J':
        result.append(S[i])

for char in result:
    print(char)