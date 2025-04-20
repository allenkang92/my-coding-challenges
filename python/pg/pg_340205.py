# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/340205
# 간단한 문제 설명 : 주어진 수를 2자리씩 잘라서 모든 부분을 더합니다.
# 해결 방법 설명 : 100으로 나누어 마지막 2자리를 구하고, 
#                나머지 자릿수는 100으로 나눈 몫으로 계속 진행합니다.
# 시간/공간 복잡도 : O(log n) (숫자의 자릿수에 비례)

number = int(input())

answer = 0

while number > 0:            # number가 0보다 클 때까지
    answer += number % 100   # 마지막 2자리를 더함
    number //= 100          # 나머지 자릿수로 진행

print(answer)