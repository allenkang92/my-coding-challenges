# 문제 링크 : https://www.acmicpc.net/problem/2741
# 간단한 문제 설명 : 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성
# 해결 방법 설명 : for문을 사용하여 1부터 N까지 출력
# 시간/공간 복잡도 : O(N)

N = int(input())

for i in range(1, N+1):
    print(i)