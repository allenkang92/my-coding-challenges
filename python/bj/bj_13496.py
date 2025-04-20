# 문제 링크 : https://www.acmicpc.net/problem/13496
# 간단한 문제 설명 : 안토니오가 기한 내에 갚을 수 있는 두캇의 총액을 계산하세요.
# 해결 방법 설명 : 각 배의 도착 시간을 계산하여 기한 내에 도착하는 배의 화물 가치를 더합니다.
# 시간/공간 복잡도 : O(nK), 여기서 n은 배의 수, K는 데이터 세트의 수

# 데이터 세트의 수 입력 받기
K = int(input())

# 각 데이터 세트 처리
for x in range(1, K + 1):
    # 배의 수, 속도, 기한 입력 받기
    n, s, d = map(int, input().split())
    
    # 총액 초기화
    total = 0
    
    # 각 배의 정보 입력 받기
    for _ in range(n):
        di, vi = map(int, input().split())
        
        # 배가 기한 내에 도착하는지 확인
        if di <= s * d:
            total += vi
    
    # 결과 출력
    print(f"Data Set {x}:")
    print(total)
    print()  # 데이터 세트 사이에 빈 줄 추가