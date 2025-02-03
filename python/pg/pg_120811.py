# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120811
# 간단한 문제 설명 : 
# 해결 방법 설명 : 
# 시간/공간 복잡도 : 

def solution(array):
    # array의 길이는 홀수. len()해도 홀수.
    answer = []
    array = sorted(array)
    
    # 중앙값을 어떻게 가져와야 하는가?
    n = len(array)
    answer = array[n//2]
    
    return answer

# def solution(array):
#     array.sort()  # in-place 정렬
#     return array[len(array) // 2]

# def solution(array):
#     array.sort()

#     n = len(array)
    
#     if n % 2 == 1:
#         return array[n // 2]
#     else:
#         return array[(n // 2) - 1]  # 또는 array[n // 2], 문제에 따라 선택

