# 문제 링크 : [https://www.acmicpc.net/problem/17912](https://www.acmicpc.net/problem/17912)
# 간단한 문제 설명 : n일 동안 매일 우주 쓰레기 개수가 주어질 때, 가장 적은 쓰레기가 있는 첫 번째 날(0-indexed)을 구하는 문제
# 해결 방법 설명 : 리스트에서 최소값을 찾아 그 인덱스를 출력
# 시간/공간 복잡도 : O(n) / O(n)

n = int(input())  # 발사 가능 일수 n을 입력받음
junk = list(map(int, input().split()))  # 각 날의 우주 쓰레기 개수를 리스트로 입력받음
print(junk.index(min(junk)))  # 가장 적은 쓰레기 개수의 첫 번째 인덱스를 출력