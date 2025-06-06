# 문제 링크 : https://www.acmicpc.net/problem/23530
# 간단한 문제 설명 : 두 수 a와 b의 합이 아닌 값 c를 출력하는 문제 (1 ≤ c ≤ 50)
# 해결 방법 설명 : 1부터 50까지의 숫자 중에서 a+b가 아닌 아무 숫자나 선택하면 됨
# 시간/공간 복잡도 : O(T), T는 테스트 케이스의 수

# 테스트 케이스 개수 입력
T = int(input())

# 각 테스트 케이스 처리
for _ in range(T):
    # 두 정수 a, b 입력
    a, b = map(int, input().split(" "))
    
    # a+b가 아닌 값 c 출력
    # 간단하게 1 출력 (a+b가 1이면 2 출력)
    if a + b == 1:
        print(2)
    else:
        print(1)