# 문제 링크 : https://www.acmicpc.net/problem/11966
# 간단한 문제 설명 : 주어진 자연수 N이 2의 제곱수인지 판별하는 문제
# 해결 방법 설명 : 0부터 30까지의 모든 2의 제곱수를 리스트에 저장한 후, N이 리스트에 포함되어 있는지 확인
# 시간/공간 복잡도 : O(1) - 2^30까지만 계산하므로 상수 시간

# 입력 받기
N = int(input())

# 2의 제곱수 리스트 생성 (2^0부터 2^30까지)
two_power = []
for i in range(0, 30 + 1):
    two_power.append(2 ** i)
    
# N이 2의 제곱수인지 확인하고 결과 출력
if N in two_power:
    print(1)
else:
    print(0)