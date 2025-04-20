# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181880
# 간단한 문제 설명 : 주어진 숫자들을 1로 만들기 위해 필요한 연산 횟수를 구합니다.
# 해결 방법 설명 : 1. 각 숫자에 대해 반복:
#                   - 짝수면 2로 나누기
#                   - 홀수면 1을 빼고 2로 나누기
#                2. 1이 될 때까지의 연산 횟수를 누적
# 시간/공간 복잡도 : O(n * log m) (n은 리스트 길이, m은 각 숫자의 최대값)

def solution(num_list):
    total_count = 0
    
    for num in num_list:        # 각 숫자에 대해
        while num > 1:          # 1이 될 때까지
            if num % 2 == 0:    # 짝수면
                num //= 2       # 2로 나누기 (정수 나눗셈 사용)
            else:               # 홀수면
                num = (num - 1) // 2  # 1 빼고 2로 나누기
            total_count += 1    # 연산 횟수 증가
            
    return total_count