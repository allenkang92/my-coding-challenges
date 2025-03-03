# 문제 링크 (주석) : https://www.acmicpc.net/problem/29340
# 간단한 문제 설명 : 두 개의 숫자 a와 b가 주어졌을 때, 각 자리 숫자를 비교하여 더 큰 값을 선택하여 새로운 숫자를 만듦
# 해결 방법 설명 : 각 자리 숫자를 비교하여 더 큰 값을 선택하고, 이를 순서대로 이어서 새로운 숫자를 출력
# 시간/공간 복잡도 : O(n) (숫자의 길이에 비례하여 시간과 공간이 소요됨)

# 입력 받기
a = input().strip()
b = input().strip()

# 결과 숫자 초기화
result = []

# 각 자리 숫자 비교
for i in range(len(a)):
    result.append(max(a[i], b[i]))

# 결과 출력
print(''.join(result))