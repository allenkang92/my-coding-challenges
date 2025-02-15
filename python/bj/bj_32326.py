# 문제 링크 (주석) : https://www.acmicpc.net/problem/32326
# 간단한 문제 설명 : 빨간 접시는 3달러, 초록 접시는 4달러, 파란 접시는 5달러인 초밥을 선택한 양에 따라 총 비용을 계산
# 해결 방법 설명 : (R * 3) + (G * 4) + (B * 5)
# 시간/공간 복잡도 : O(1)

R = int(input())
G = int(input())
B = int(input())

print((R * 3) + (G * 4) + (B * 5))