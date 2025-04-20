# 문제 링크 : https://www.acmicpc.net/problem/27222
# 간단한 문제 설명 : 역도 선수의 훈련 일지에서 근육량 증가를 계산
# 해결 방법 설명 : 훈련한 날에 체중이 증가한 경우, 증가량을 근육량 증가로 계산
# 시간/공간 복잡도 : O(n) (날짜 수에 비례하여 시간과 공간이 소요됨)

# 입력 받기
n = int(input())
training_days = list(map(int, input().split()))
weights = [tuple(map(int, input().split())) for _ in range(n)]

# 근육량 증가 초기화
total_muscle_gain = 0

# 각 날짜에 대해 근육량 증가 계산
for i in range(n):
    if training_days[i] == 1:  # 훈련한 날
        morning, evening = weights[i]
        if evening > morning:  # 체중이 증가한 경우
            total_muscle_gain += evening - morning

# 결과 출력
print(total_muscle_gain)