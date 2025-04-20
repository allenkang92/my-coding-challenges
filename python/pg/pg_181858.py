# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181858
# 간단한 문제 설명 : arr에서 순서대로 중복되지 않는 k개의 수를 선택합니다.
#                  k개를 채우지 못하면 나머지를 -1로 채웁니다.
# 해결 방법 설명 : 1. arr를 순회하며 중복되지 않는 숫자만 새 리스트에 추가
#                 2. k개가 채워지면 반복 중단
#                 3. k개 미만이면 -1로 채움
# 시간/공간 복잡도 : O(n) (n은 arr의 길이)

def solution(arr, k):
    answer = []
    check_num = []
    for i in arr:
        if len(check_num) == k:   # k개가 채워지면 중단
            break
        if i not in check_num:    # 중복되지 않는 수만 추가
            check_num.append(i)
    if len(check_num) < k:        # k개 미만이면 -1로 채움
        for j in range(k - len(check_num)):
            check_num.append(-1)
    return check_num