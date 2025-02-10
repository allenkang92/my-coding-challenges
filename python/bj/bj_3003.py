# 문제 링크 (주석) : https://www.acmicpc.net/problem/3003
# 간단한 문제 설명 : 체스 피스의 정확한 개수와 현재 가지고 있는 개수를 비교하여
#                  추가하거나 제거해야 할 피스의 개수를 구합니다.
# 해결 방법 설명 : 1. 정확한 체스 피스 개수(1,1,2,2,2,8)와 현재 피스 개수를 비교
#                2. 각 피스별로 차이를 계산하여 결과 리스트에 저장
#                3. 결과 리스트를 공백으로 구분하여 출력
# 시간/공간 복잡도 : O(1) (고정된 크기의 리스트 처리)

# 현재 가지고 있는 체스 피스 개수 입력 받기
chess_w = list(map(int, input().split(" ")))

# 체스 피스의 정확한 개수 (킹, 퀸, 룩, 비숍, 나이트, 폰 순서)
chess_b = [1, 1, 2, 2, 2, 8]

# 결과를 저장할 리스트 초기화
result = []
for i in range(len(chess_b)):
    if chess_b[i] == chess_w[i]:      # 현재 개수가 정확한 경우
        result.append(0)
    elif chess_b[i] != chess_w[i]:     # 현재 개수가 다른 경우
        result.append(chess_b[i] - chess_w[i])  # 차이를 계산하여 저장

# 결과 출력 (*를 사용하여 리스트를 공백으로 구분하여 출력)
print(*result)

# # 현재 가지고 있는 체스 피스 개수 입력
# chess_w = list(map(int, input().split()))

# # 정확한 체스 피스 개수
# chess_b = [1, 1, 2, 2, 2, 8]

# # 각 피스별로 필요한 개수 계산
# result = []
# for i in range(len(chess_b)):
#     result.append(chess_b[i] - chess_w[i])  # 필요한 개수 = 정확한 개수 - 현재 개수

# # 결과 출력 (*를 사용하여 리스트를 공백으로 구분하여 출력)
# print(*result)