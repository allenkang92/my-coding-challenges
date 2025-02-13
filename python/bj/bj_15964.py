# 문제 링크 (주석) : https://www.acmicpc.net/problem/15964
# 간단한 문제 설명 : A @ B = (A + B) * (A - B)를 계산하는 문제
# 해결 방법 설명 : 입력받은 두 정수 A, B에 대해 (A + B) * (A - B)를 계산하여 출력
# 시간/공간 복잡도 : O(1)

A, B = map(int, input().split())

# A @ B = (A + B) * (A - B)
print((A + B) * (A - B))