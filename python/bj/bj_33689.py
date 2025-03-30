# 문제 링크 : https://www.acmicpc.net/problem/33689
# 간단한 문제 설명 : 주어진 N개의 대회 이름 후보 중, C로 시작하는 문자열의 개수를 세는 문제
# 해결 방법 설명 : 각 문자열의 첫 글자가 'C'인지 확인하여 개수를 세기
# 시간/공간 복잡도 : O(N)

# 입력 처리
N = int(input())

# C로 시작하는 대회 이름의 개수를 저장할 변수
count = 0

# N개의 대회 이름 후보를 확인
for _ in range(N):
    # 대회 이름 입력
    candidate = input().strip()
    
    # 첫 글자가 'C'인지 확인
    if candidate[0] == 'C':
        count += 1  # C로 시작하면 개수 증가

# 결과 출력
print(count)