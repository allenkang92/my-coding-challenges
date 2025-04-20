# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/340200
# 간단한 문제 설명 : 닉네임의 특정 문자를 규칙에 따라 변경하고 길이를 조정합니다.
# 해결 방법 설명 : 1. l->I, w->vv, W->VV, O->0 로 변경
#                2. 길이가 4 미만이면 'o'를 추가
#                3. 길이가 8 초과면 잘라냄
# 시간/공간 복잡도 : O(n) (문자열 길이에 비례)

def solution(nickname):
    answer = ""
    for letter in nickname:
        if letter == "l":
            answer += "I"
        elif letter == "w":
            answer += "vv"
        elif letter == "W":
            answer += "VV"
        elif letter == "O":
            answer += "0"
        else:
            answer += letter
    if len(answer) < 4:                    # 3에서 4로 수정
        answer += ("o" * (4-len(answer)))  # 부족한 만큼 'o' 추가
    if len(answer) > 8:
        answer = answer[:8]
    return answer