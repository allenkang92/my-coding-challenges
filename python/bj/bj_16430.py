# 문제 링크 : https://www.acmicpc.net/problem/16430
# 간단한 문제 설명 : A/B kg의 치즈를 도난당한 뒤 남은 치즈의 무게를 기약분수 형태로 출력
# 해결 방법 설명 : 남은 치즈 = 1 - (A/B) = (B-A)/B
# 시간/공간 복잡도 : O(1)

A, B = map(int, input().split())
print(B - A, B)