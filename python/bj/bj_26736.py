# 문제 링크 : https://www.acmicpc.net/problem/26736
# 간단한 문제 설명 : 주어진 문자열에서 A와 B의 개수를 세어 각 팀의 골 수를 출력
# 해결 방법 설명 : 문자열을 순회하며 A와 B의 개수를 각각 계산
# 시간/공간 복잡도 : O(n) (문자열의 길이에 비례하여 시간과 공간이 소요됨)

# 입력 받기
line = input()

# 골 수 초기화
X = 0  # Algogród 팀의 골 수
Y = 0  # Bajtocja 팀의 골 수

# 문자열 순회하며 골 수 계산
for i in line:
    if i == "A":
        X += 1
    elif i == "B":
        Y += 1

# 결과 출력
print(f"{X} : {Y}")