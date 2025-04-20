# 문제 링크 : https://www.acmicpc.net/problem/31450
# 간단한 문제 설명 : M개의 메달을 K명의 아이들에게 모두 나누어 줄 수 있는지 (모두 같은 수량) 판별
# 해결 방법 설명 : M을 K로 나누었을 때 나머지가 0이면 모든 아이가 같은 수의 메달을 받을 수 있음
# 시간/공간 복잡도 : O(1)

M, K = map(int, input().split(" "))

if M % K == 0:
    print("Yes")
else:
    print("No")