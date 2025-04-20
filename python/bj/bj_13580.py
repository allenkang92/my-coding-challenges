# 문제 링크 : https://www.acmicpc.net/problem/13580
# 간단한 문제 설명 : 세 크레딧을 사용하여 시간 여행을 한 후 현재로 돌아올 수 있는지 판단하세요.
# 해결 방법 설명 : 세 크레딧의 조합을 확인하여 현재로 돌아올 수 있는지 판단합니다.
# 시간/공간 복잡도 : O(1)

# 입력 받기
A, B, C = map(int, input().split())

# 현재로 돌아올 수 있는지 판단
if A == B or B == C or A == C:  # 두 크레딧이 같으면 가능
    print("S")
elif A + B == C or A + C == B or B + C == A:  # 두 크레딧의 합이 나머지 하나와 같으면 가능
    print("S")
else:
    print("N")