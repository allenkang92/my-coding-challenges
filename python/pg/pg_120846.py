# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120846
# 간단한 문제 설명 : 
#   약수의 개수가 세 개 이상인 수를 합성수라고 합니다.
#   자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return합니다.
#
# 해결 방법 설명 : 
#   - 1부터 n까지 각 수에 대해, 1부터 해당 수까지의 약수의 개수를 센다.
#   - 약수의 개수가 3개 이상이면 합성수로 판단하여 개수를 증가시킵니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(n^2) (n은 n의 값, n 최대 100이므로 충분함)
#   - 공간 복잡도: O(1)

def solution(n):
    composite_count = 0
    for num in range(1, n + 1):
        divisor_count = 0
        for div in range(1, num + 1):
            if num % div == 0:
                divisor_count += 1
        if divisor_count >= 3:
            composite_count += 1
    return composite_count