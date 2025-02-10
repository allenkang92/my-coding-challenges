# 문제 링크 (주석) : https://www.acmicpc.net/problem/11720
# 간단한 문제 설명 : 
#   N개의 숫자가 공백 없이 주어질 때 모든 숫자의 합을 구하는 프로그램
#
# 해결 방법 설명 : 
#   - 첫 줄에서 숫자 개수 N 입력
#   - 둘째 줄의 문자열을 한 글자씩 정수로 변환하여 합산
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(N) - N개의 숫자 처리
#   - 공간 복잡도: O(N) - N길이의 문자열 저장

N = int(input())
nums = input()  # 문자열로 입력받음
total = 0

for num in nums:
    total += int(num)  # 각 문자를 정수로 변환하여 더함

print(total)