# 문제 링크 (주석) : https://www.acmicpc.net/problem/11945
# 간단한 문제 설명 : 
#   입력으로 주어진 붕어빵의 모양을 좌우 반전시켜 출력하는 문제입니다.
#
# 해결 방법 설명 :            
#   각 행의 문자열을 반전시켜서 출력하면 됩니다.
#
# 시간/공간 복잡도 : O(N*M)

N, M = map(int, input().split(" "))

for _ in range(N):
    line = input().strip()
    print(line[::-1])