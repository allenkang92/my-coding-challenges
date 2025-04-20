# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181898
# 간단한 문제 설명 : idx 이후에서 가장 먼저 나오는 1의 인덱스를 찾습니다.
# 해결 방법 설명 : idx부터 시작하여 배열을 순회하면서 처음 만나는 1의 인덱스를 반환합니다.
# 시간/공간 복잡도 : O(n) (n은 배열의 길이)

def solution(arr, idx):
    for i in range(idx, len(arr)):  # idx부터 배열 끝까지 순회
        if arr[i] == 1:             # 1을 발견하면
            return i                 # 해당 인덱스 반환
    return -1                       # 1을 못 찾으면 -1 반환