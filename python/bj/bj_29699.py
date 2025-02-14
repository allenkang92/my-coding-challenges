# 문제 링크 (주석) : https://www.acmicpc.net/problem/29699
# 간단한 문제 설명 : "WelcomeToSMUPC" 문자열이 반복될 때 N번째 글자를 찾는 문제
# 해결 방법 설명 : N을 문자열 길이로 나눈 나머지를 이용하여 N번째 글자를 찾음
# 시간/공간 복잡도 : O(1)

N = int(input())

ch = "WelcomeToSMUPC"

print(ch[(N-1) % len(ch)])