# 문제 링크 : https://www.acmicpc.net/problem/2845
# 간단한 문제 설명 : 1m²당 L명, 파티 장소 넓이 P이 주어지고, 기사에 적힌 참가 인원과의 차이를 출력
# 해결 방법 설명 : (기사에 적힌 인원) - (L * P)
# 시간/공간 복잡도 : O(1)

L, P = map(int, input().split(" "))
articles = list(map(int, input().split(" ")))  # 기사에 적힌 참가자 수 5개

expected = L * P
differences = [(num - expected) for num in articles]

print(*differences)