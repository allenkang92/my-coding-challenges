# 문제 링크 (주석) : https://www.acmicpc.net/problem/2742
# 간단한 문제 설명 : 자연수 N이 주어지면, N부터 1까지 한 줄에 하나씩 출력한다.
# 해결 방법 설명 : for문을 역순으로 사용하거나 range(N, 0, -1)을 사용하여 출력한다.
# 시간/공간 복잡도 : O(N)

N = int(input())

for i in range(N, 0, -1):
    print(i)