# 문제 링크 (주석) : https://www.acmicpc.net/problem/21591
# 간단한 문제 설명 : 노트북 스티커가 노트북에 맞는지 확인하는 문제
# 해결 방법 설명 : 스티커의 크기가 노트북 크기에서 2cm를 뺀 값보다 작거나 같은지 확인
# 시간/공간 복잡도 : O(1) (입력 크기에 관계없이 일정한 시간과 공간이 소요됨)

# 입력 받기
wc, hc, ws, hs = map(int, input().split())

# 조건 확인
if ws <= wc - 2 and hs <= hc - 2:
    print(1)
else:
    print(0)