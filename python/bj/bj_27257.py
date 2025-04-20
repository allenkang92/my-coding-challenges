# 문제 링크 : https://www.acmicpc.net/problem/27257
# 간단한 문제 설명 : 주어진 숫자 k에서 끝에 있는 0을 제외한 나머지 0의 개수를 세는 문제
# 해결 방법 설명 : 숫자 k에서 끝의 0을 제거하고, 나머지 0의 개수를 셈
# 시간/공간 복잡도 : O(n) (n은 숫자 k의 길이)

# 입력 받기
k = input().strip()

# 끝의 0 제거
k = k.rstrip('0')

# 0의 개수 세기
count = k.count('0')

# 결과 출력
print(count)