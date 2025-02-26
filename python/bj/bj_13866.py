# 문제 링크 (주석) : https://www.acmicpc.net/problem/13866
# 간단한 문제 설명 : 4명의 스킬 레벨이 주어졌을 때, 두 팀으로 나누어 스킬 레벨 합계 차이의 최솟값을 구하세요.
# 해결 방법 설명 : 가능한 모든 팀 조합을 고려하여 최소 차이를 계산합니다.
# 시간/공간 복잡도 : O(1)

# 네 명의 스킬 레벨 입력
A, B, C, D = map(int, input().split())

# 가능한 팀 조합의 차이 계산
diff1 = abs((A + D) - (B + C))  # A와 D, B와 C 팀
diff2 = abs((A + C) - (B + D))  # A와 C, B와 D 팀
diff3 = abs((A + B) - (C + D))  # A와 B, C와 D 팀

# 최소 차이 출력
print(min(diff1, diff2, diff3))