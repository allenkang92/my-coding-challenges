# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120842
# 간단한 문제 설명 : 1차원 배열을 n개씩 그룹화하여 2차원 배열로 변환합니다.
# 해결 방법 설명 : 1. num_list를 n개씩 슬라이싱하여 리스트에 저장
#                2. range(0, len(num_list), n)으로 n간격으로 인덱스 생성
#                3. 각 인덱스에서 n개씩 슬라이싱하여 하위 리스트 생성
# 시간/공간 복잡도 : O(n) (n은 num_list의 길이)

def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer