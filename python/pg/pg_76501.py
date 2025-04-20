# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/76501
# 간단한 문제 설명 : absolutes 배열의 각 숫자에 signs 배열의 부호를 적용하여 합계를 계산합니다.
# 해결 방법 설명 : signs 배열을 순회하면서 True면 양수, False면 음수를 absolutes에 적용합니다.
# 시간/공간 복잡도 : O(n)

def solution(absolutes, signs):
    for i in range(len(signs)):
        if signs[i] == True:
            absolutes[i] = int(absolutes[i])
        elif signs[i] == False: 
            absolutes[i] = int(-absolutes[i])
    return sum(absolutes)

    # def solution(absolutes, signs):
    # answer = 0
    # for i in range(len(signs)):
    #     if signs[i]:
    #         answer += absolutes[i]
    #     else:
    #         answer -= absolutes[i]
    # return answer