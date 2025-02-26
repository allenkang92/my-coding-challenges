# 문제 링크 (주석) : https://www.acmicpc.net/problem/8760
# 간단한 문제 설명 : 주어진 방의 크기에 따라 최대 수용 가능한 관광객 수를 계산하는 프로그램입니다.
# 해결 방법 설명 : 방의 총 칸 수를 2로 나누어 최대 수용 가능한 관광객 수를 구합니다.
# 시간/공간 복잡도 : O(1)

T = int(input())  # 테스트 케이스 수

for _ in range(T):
    W, K = map(int, input().split())
    # 최대 수용 가능한 관광객 수
    max_tourists = (W * K) // 2
    print(max_tourists)