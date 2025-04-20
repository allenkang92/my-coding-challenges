# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/250126
# 간단한 문제 설명 : 창고의 물건들을 종류별로 합치고, 가장 많은 개수를 가진 물건을 찾습니다.
# 해결 방법 설명 : 1. 같은 물건은 하나의 위치에 개수를 합칩니다.
#                2. 새로운 물건은 새로운 위치에 추가합니다.
#                3. 가장 개수가 많은 물건을 찾아 반환합니다.
# 시간/공간 복잡도 : O(n) (storage의 길이에 비례)

def solution(storage, num):
    clean_storage = []
    clean_num = []
    for i in range(len(storage)):
        if storage[i] in clean_storage:
            pos = clean_storage.index(storage[i])
            clean_num[pos] += num[i]  # 이미 있는 물건의 개수를 더함
        else:
            clean_storage.append(storage[i])  # 새로운 물건 추가
            clean_num.append(num[i])  # 새로운 물건의 개수 추가
            
            
    max_num = max(clean_num)
    answer = clean_storage[clean_num.index(max_num)]
    return answer