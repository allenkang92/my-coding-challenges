# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120808
# 간단한 문제 설명 :
#   두 분수를 더한 값을 기약분수 형태로 반환
#
# 해결 방법 설명 :
#   - 분자: numer1*denom2 + numer2*denom1
#   - 분모: denom1*denom2
#   - 최대공약수(GCD)로 분모와 분자를 나누어 기약분수로 만듦
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(log(min(a, b))) - gcd 계산
#   - 공간 복잡도: O(1) - 상수 공간

def solution(numer1, denom1, numer2, denom2):
    sum_numer = numer1 * denom2 + numer2 * denom1
    sum_denom = denom1 * denom2
    
    a, b = sum_numer, sum_denom
    while b != 0:
        a, b = b, a % b
    
    sum_numer //= a
    sum_denom //= a
    return [sum_numer, sum_denom]