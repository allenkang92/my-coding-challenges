# 문제 링크 : https://www.acmicpc.net/problem/30143
# 간단한 문제 설명 : 주어진 테스트 케이스에 대해, 각 쿠키 더미의 쿠키 수를 계산하고 총 쿠키 수를 구함
# 해결 방법 설명 : 등차수열의 합 공식을 사용하여 총 쿠키 수를 계산
# 시간/공간 복잡도 : O(T) (T는 테스트 케이스의 수)

# 입력 처리
T = int(input())
for _ in range(T):
    N, A, D = map(int, input().split())
    
    # 총 쿠키 수 계산
    total_cookies = N * (2 * A + (N - 1) * D) // 2
    
    # 결과 출력
    print(total_cookies)