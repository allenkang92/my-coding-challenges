# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120840
# 간단한 문제 설명 : balls개의 서로 다른 구슬 중 share개를 고르는 조합의 수를 계산합니다.
# 해결 방법 설명 : 조합 공식 nCr = n!/(r!(n-r)!)을 사용합니다.
#                팩토리얼 계산을 위해 반복문을 사용하고,
#                balls개 중 share개를 선택하는 경우의 수를 계산합니다.
# 시간/공간 복잡도 : O(n) (n은 balls의 크기)

def solution(balls, share):
    answer = 0
    n_fac = 1
    m_fac = 1
    m_sub = balls - share
    m_sub_fac = 1
    
    # n! 계산
    for i in range(1, balls+1):
        n_fac *= i
        
    # m! 계산
    for j in range(1, share+1):
        m_fac *= j
        
    # (n-m)! 계산
    for k in range(1, m_sub+1):
        m_sub_fac *= k
        
    # 조합 공식 nCr = n!/(r!(n-r)!) 적용
    answer = n_fac / (m_sub_fac * m_fac)
    return answer