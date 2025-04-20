# 문제 링크 : https://www.acmicpc.net/problem/32775
# 간단한 문제 설명 : 고속철도와 항공편 중 어느 교통수단을 더 많이 이용하는지 판단하는 문제
# 해결 방법 설명 : 고속철도 소요 시간이 4시간(240분) 이하이면 고속철도, 아니면 항공편을 이용
# 시간/공간 복잡도 : O(1)

S = int(input())  # 고속철도 소요 시간 (분)
F = int(input())  # 항공편 소요 시간 (분)
 
if F < S:
    print("flight")
else:
    print("high speed rail")