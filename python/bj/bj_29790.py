# 문제 링크 : https://www.acmicpc.net/problem/29790
# 문제 설명:
#   임스는 비공식 메이플컵 출제진 지원 자격을 평가하기 위한 두 가지 조건을 정했다.
#   조건은 다음과 같다:
#     1. 백준에서 1,000문제 이상 해결했는가? (N)
#     2. 메이플스토리에서 유니온 레벨이 8,000 이상이거나 최고 레벨이 260 이상인가? (U, L)
#
#   두 조건을 모두 만족하면 "Very Good"
#   백준 조건만 만족하면 "Good"
#   어느 조건도 만족하지 않으면 "Bad"를 출력한다.
#
# 입력:
#   첫 번째 줄에 문제 해결 개수 N, 유니온 레벨 U, 최고 레벨 L이 공백으로 구분되어 주어진다.
#   (1 ≤ N ≤ 130,000, 1 ≤ U ≤ 12,500, 1 ≤ L ≤ 300)
#
# 출력:
#   조건에 따라 "Very Good", "Good", "Bad" 중 하나를 출력한다.
#
# 해결 방법:
#   조건에 따라 순서대로 판단한다.
#
# 시간/공간 복잡도: O(1)

N, U, L = map(int, input().split())

if N >= 1000 and (U >= 8000 or L >= 260):
    print("Very Good")
elif N >= 1000:
    print("Good")
else:
    print("Bad")