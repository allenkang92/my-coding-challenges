# 문제 링크 (주석) : https://www.acmicpc.net/problem/17548
# 간단한 문제 설명 : 주어진 문자열에서 'e'의 개수를 두 배로 늘려 응답하는 문제
# 해결 방법 설명 : 문자열을 순회하며 'e'의 개수를 세고, 두 배로 늘려 새로운 문자열 생성
# 시간/공간 복잡도 : O(n) (문자열 길이에 비례하는 시간과 공간이 소요됨)

# 입력 받기
s = input().strip()  # 입력 문자열

# 'e'의 개수 세기
e_count = s.count('e')

# 새로운 문자열 생성
response = s.replace('e', 'e' * 2)  # 'e'를 두 배로 늘림

# 결과 출력
print(response)