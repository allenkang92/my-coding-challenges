# 문제 링크 (주석) : https://www.acmicpc.net/problem/5357
# 문제 설명:
#   주어진 문자열에서 인접한 중복 문자를 제거하는 문제입니다.
#   예를 들어 "AAABB"는 "AB"가 되어야 합니다.
#
# 해결 방법 설명:
#   각 데이터 세트(문자열)를 순회하면서, 이전에 추가된 문자와 비교하여 다른 경우에만
#   결과 문자열에 추가합니다.
#
# 시간/공간 복잡도 : O(n) (문자열의 길이를 n이라 할 때)
 
T = int(input())

for _ in range(T):
    line = input().strip()
    deduped = ""
    for ch in line:
        if not deduped or deduped[-1] != ch:
            deduped += ch
    print(deduped)