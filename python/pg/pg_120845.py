# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120845
# 간단한 문제 설명 :
#   주사위의 개수를 구하는 문제입니다. 상자(box)의 가로, 세로, 높이에
#   주사위 모서리 길이 n을 나눈 몫을 모두 곱하면 상자에 들어갈 수 있는 주사위의 최대 개수입니다.
#
# 해결 방법 설명 :
#   - 상자의 각 치수를 주사위의 모서리 길이 n으로 나눈 몫을 구합니다.
#   - 세 개의 몫을 모두 곱하면 상자 내부에 들어갈 수 있는 주사위의 개수를 구할 수 있습니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(1)
#   - 공간 복잡도: O(1)

def solution(box, n):
    answer = int(box[0] / n) * int(box[1] / n) * int(box[2] / n)
    return answer