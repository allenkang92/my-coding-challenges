# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181896
# 간단한 문제 설명 : 정수 리스트에서 첫 번째로 나오는 음수의 인덱스를 반환하고,
#                  음수가 없다면 -1을 반환합니다.
# 해결 방법 설명 : 리스트를 순회하며 음수를 찾고, index() 메서드로 해당 음수의 위치를 찾습니다.
#                음수가 없는 경우 -1을 반환합니다.
# 시간/공간 복잡도 : O(n) (리스트 길이에 비례)
# 주의사항 : index() 메서드는 값이 여러 개 있을 때 첫 번째 위치만 반환하므로,
#          실제로 원하는 '처음 등장하는 음수의 위치'와 다를 수 있습니다.

def solution(num_list):
    answer = 0
    for i in num_list:
        if i < 0:
            answer = num_list.index(i)  # 주의: index()는 첫 번째 등장 위치만 반환
            break
        for j in range(-10, 100+1):     # 불필요한 이중 루프 - 제거 가능
            if j not in num_list:
                answer = -1
    return answer