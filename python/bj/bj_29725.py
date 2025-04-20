# 문제 링크 : https://www.acmicpc.net/problem/29725
# 간단한 문제 설명 : 체스판의 상태를 입력받아 백의 기물 점수 합에서 흑의 기물 점수 합을 뺀 값을 계산
# 해결 방법 설명 : 각 기물의 점수를 합산하고, 백의 점수에서 흑의 점수를 뺀 값을 출력
# 시간/공간 복잡도 : O(1) (체스판 크기가 고정되어 있으므로 상수 시간과 공간이 소요됨)

# 기물 점수 정의
piece_scores = {
    'K': 0, 'k': 0,
    'P': 1, 'p': 1,
    'N': 3, 'n': 3,
    'B': 3, 'b': 3,
    'R': 5, 'r': 5,
    'Q': 9, 'q': 9
}

# 백과 흑의 점수 초기화
white_score = 0
black_score = 0

# 체스판 입력 받기
for _ in range(8):
    row = input().strip()
    for piece in row:
        if piece in piece_scores:
            if piece.isupper():
                white_score += piece_scores[piece]
            else:
                black_score += piece_scores[piece]

# 결과 출력
print(white_score - black_score)