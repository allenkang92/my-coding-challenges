# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/250128
# 간단한 문제 설명 : 가채점한 점수와 실제 점수를 비교하여 같은지 다른지 판단합니다.
# 해결 방법 설명 : 1. numbers 배열의 각 학생 번호에 대해
#                2. 해당 학생의 가채점 점수와 실제 점수를 비교
#                3. 같으면 "Same", 다르면 "Different" 반환
# 시간/공간 복잡도 : O(n) (n은 numbers의 길이)

def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i]-1]:  # numbers[i]-1로 실제 인덱스 계산
            answer.append("Same")
        else:
            answer.append("Different")
    
    return answer