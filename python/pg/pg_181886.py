# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181886
# 간단한 문제 설명 : 놀이기구 탑승 대기줄의 이름 리스트 names에서, 앞에서부터 5명씩 그룹을 묶었을 때 각 그룹의
#                가장 앞에 있는 사람의 이름을 담은 리스트를 반환합니다.
# 해결 방법 설명 : 리스트 슬라이싱(names[::5])을 사용하여 0번, 5번, 10번, ... 인덱스의 이름들을 추출합니다.
# 시간/공간 복잡도 : O(n)

def solution(names):
    # 슬라이싱을 통해 0번 인덱스부터 5명씩 건너뛰며 그룹의 첫 번째 원소 선택
    answer = names[::5]
    return answer