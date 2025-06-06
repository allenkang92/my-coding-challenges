# 문제 링크 : https://www.acmicpc.net/problem/20053
# 간단한 문제 설명 : 여러 개의 테스트 케이스에 대해 각 정수 리스트의 최솟값과 최댓값을 구하는 문제
# 해결 방법 설명 : 파이썬 내장 함수 min()과 max()를 사용하여 각 테스트 케이스의 최솟값과 최댓값을 구함
# 시간/공간 복잡도 : O(T*N), T는 테스트 케이스 수, N은 각 테스트 케이스의 정수 개수

# 테스트 케이스 개수 T 입력
T = int(input())

# 각 테스트 케이스 처리
for _ in range(T):
    # 정수의 개수 N 입력
    N = int(input())
    
    # N개의 정수를 리스트로 입력받음
    N_list = list(map(int, input().split(" ")))
    
    # 최솟값과 최댓값을 구하여 출력
    print(min(N_list), max(N_list))