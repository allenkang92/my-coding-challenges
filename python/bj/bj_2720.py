# 문제 링크 : https://www.acmicpc.net/problem/2720
# 간단한 문제 설명 : 
#   거스름돈을 동전으로 거슬러 줄 때 각 동전의 개수를 계산하는 문제입니다.
#   Quarter($0.25), Dime($0.10), Nickel($0.05), Penny($0.01) 순으로 계산합니다.
#
# 해결 방법 설명 : 
#   - 각 테스트 케이스마다 센트 단위의 거스름돈을 입력받습니다.
#   - 큰 단위의 동전부터 차례로 나누어 개수를 계산합니다.
#   - 각 동전을 사용한 후 남은 금액으로 다음 동전을 계산합니다.
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(T) (T는 테스트 케이스 수)
#   - 공간 복잡도: O(1)

T = int(input())  # 테스트 케이스 수

Quarter = 25  # $0.25
Dime = 10     # $0.10
Nickel = 5    # $0.05
Penny = 1     # $0.01

for _ in range(T):
    C = int(input())  # 센트 단위 거스름돈
    
    # 각 동전 개수 계산
    q_count = C // Quarter
    C %= Quarter
    
    d_count = C // Dime
    C %= Dime
    
    n_count = C // Nickel
    C %= Nickel
    
    p_count = C // Penny
    
    print(q_count, d_count, n_count, p_count)