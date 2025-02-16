# 문제 링크 (주석) : https://www.acmicpc.net/problem/31654
# 간단한 문제 설명 : 주어진 3개의 정수 A, B, C가 있을 때, A + B가 C와 같은지 확인 후, 맞으면 "correct!", 틀리면 "wrong!"를 출력
# 해결 방법 설명 : A + B와 C를 비교
# 시간/공간 복잡도 : O(1)

A, B, C = map(int, input().split(" "))

if A + B == C:
    print("correct!")
else:
    print("wrong!")