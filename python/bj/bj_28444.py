# 문제 링크 (주석) : https://www.acmicpc.net/problem/28444
# 간단한 문제 설명 : HI-ARC 수식의 결과값을 계산하는 문제
# 해결 방법 설명 : 주어진 H, I, A, R, C 값을 이용하여 (H * I) - (A * R * C)를 계산
# 시간/공간 복잡도 : O(1)

H, I, A, R, C = map(int, input().split(" "))

first = H * I
second = A * R * C
result = first - second

print(result)