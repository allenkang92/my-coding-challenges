# 문제 링크 : https://www.acmicpc.net/problem/32684
# 간단한 문제 설명 : 장기 게임에서 두 플레이어의 점수를 계산하여 현재 점수가 더 높은 플레이어를 출력
# 해결 방법 설명 : 각 플레이어의 잃어버린 기물 수를 기반으로 점수를 계산하고, 초기 점수를 고려하여 결과를 출력
# 시간/공간 복잡도 : O(1)

# 초기 기물 개수 (차, 포, 마, 상, 사, 졸/병)
original_counts = [2, 2, 2, 2, 2, 5]
piece_scores = [13, 7, 5, 3, 3, 2]

# 입력 처리
chick_remaining = list(map(int, input().split()))  # 척이의 남은 기물 수
eunkyu_remaining = list(map(int, input().split()))  # 은규의 남은 기물 수

# 잃어버린 기물 계산 함수
def calculate_lost_score(remaining, original, scores):
    lost = [original[i] - remaining[i] for i in range(6)]
    return sum(lost[i] * scores[i] for i in range(6))

# 점수 계산
chick_score = 72 - calculate_lost_score(chick_remaining, original_counts, piece_scores)
eunkyu_score = 73.5 - calculate_lost_score(eunkyu_remaining, original_counts, piece_scores)

# 결과 출력
print("cocjr0208" if chick_score > eunkyu_score else "ekwoo")