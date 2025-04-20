# 문제 링크 : https://www.acmicpc.net/problem/25494
# 간단한 문제 설명:
#   세 양의 정수 a, b, c가 주어질 때, 다음 조건을 만족하는 정수 쌍 (x, y, z)의 개수를 구하는 문제
#   - 1 ≤ x ≤ a
#   - 1 ≤ y ≤ b
#   - 1 ≤ z ≤ c
#   - (x mod y) = (y mod z) = (z mod x)
#
# 해결 방법 설명:
#   브루트 포스(완전 탐색) 접근 방식으로 모든 가능한 (x, y, z) 조합을 확인
#   문제의 조건을 만족하는 경우를 카운팅한다.
#   
#   최적화 관점에서 살펴보면:
#   (x mod y) = (y mod z) = (z mod x)가 성립하려면 x, y, z가 모두 같은 값인 경우가 해당
#   따라서 min(a, b, c)가 정답이 됨
#            
# 시간/공간 복잡도: O(a*b*c) - 브루트 포스 방식 / O(min(a,b,c)) - 최적화 후

T = int(input())
for _ in range(T):
    a, b, c = map(int, input().split(" "))
    count = 0
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            for z in range(1, c + 1):
                if (x % y) == (y % z) == (z % x):
                    count += 1
    print(count)