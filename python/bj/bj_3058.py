# 문제 링크 : https://www.acmicpc.net/problem/3058
# 간단한 문제 설명 : 7개의 자연수 중 짝수를 찾아 합과 최솟값을 구하는 문제
# 해결 방법 설명 : 주어진 7개 숫자 중 짝수만 필터링하여 합과 최솟값을 계산
# 시간/공간 복잡도 : O(1) - 입력이 항상 7개로 고정되어 있음

# 테스트 케이스 수 입력
T = int(input())

# 각 테스트 케이스 처리
for _ in range(T):
    # 7개의 자연수 입력 받기
    N_list = list(map(int, input().split(" ")))
    # 짝수를 저장할 빈 리스트 생성
    Even_list = list()
    # 각 숫자를 확인하여 짝수만 리스트에 추가
    for n in N_list:
        if n % 2 == 0:
            Even_list.append(n)
    # 결과 출력: 짝수의 합과 최솟값
    print(sum(Even_list), min(Even_list))