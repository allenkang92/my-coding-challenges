# 문제 링크 : https://www.acmicpc.net/problem/32369
# 간단한 문제 설명 : 양파 실험을 시뮬레이션하여 '칭찬 양파'와 '비난 양파'의 최종 길이를 계산
# 해결 방법 설명 : 매일 칭찬과 비난을 적용하고, 조건에 따라 역할을 바꾸거나 길이를 조정
# 시간/공간 복잡도 : O(N)

# 입력 처리
N, A, B = map(int, input().split())  # N일, A(칭찬 증가량), B(비난 증가량) 입력

# 초기화
praise_onion = 1  # 칭찬 양파의 초기 길이
blame_onion = 1   # 비난 양파의 초기 길이

# 시뮬레이션
for _ in range(N):
    # 칭찬과 비난 적용
    praise_onion += A
    blame_onion += B

    # 조건에 따라 역할 바꾸기 또는 길이 조정
    if blame_onion > praise_onion:
        praise_onion, blame_onion = blame_onion, praise_onion  # 역할 바꾸기
    elif blame_onion == praise_onion:
        blame_onion -= 1  # 비난 양파의 길이를 1만큼 자르기

# 결과 출력
print(praise_onion, blame_onion)