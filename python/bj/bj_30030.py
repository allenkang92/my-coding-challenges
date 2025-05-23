# 문제 링크 : https://www.acmicpc.net/problem/30030
# 간단한 문제 설명 : 부가가치세 10%가 포함된 가격 B가 주어졌을 때, 부가가치세를 제외한 가격 A를 구하는 문제
# 해결 방법 설명 : B = A + 0.1A = 1.1A 이므로, A = B / 1.1 = 10B / 11
# 시간/공간 복잡도 : O(1)

B = int(input())
# 10B / 11 =  A
A = 10 * B / 11
print(int(A))