# 문제 링크 (주석) : https://www.acmicpc.net/problem/13597
# 간단한 문제 설명 : 두 장의 카드가 주어졌을 때, 세 번째 카드의 값을 선택하여 이길 확률을 최대화하세요.
# 해결 방법 설명 : 두 카드 중 더 높은 값을 선택하거나, 두 카드가 같다면 같은 값을 선택합니다.
# 시간/공간 복잡도 : O(1)

# 두 카드의 값 입력
A, B = map(int, input().split())

# 세 번째 카드의 값 선택
if A == B:
    result = A  # 트리오를 만듦
else:
    result = max(A, B)  # 더 높은 값을 선택

# 결과 출력
print(result)