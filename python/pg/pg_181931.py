# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181931  
# 간단한 문제 설명 : 첫째항이 a, 공차가 d인 등차수열에서 included[i]가 true인 항들만 더한 값을 구합니다.
# 해결 방법 설명 : included 배열을 순회하면서, true인 경우에만
#                해당 위치의 등차수열 항(a + d*i)을 더합니다.
# 시간/공간 복잡도 : O(n) (included 배열의 길이에 비례)

def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i] == True:
            answer += a + (d * i)
    return answer