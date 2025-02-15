# 문제 링크 (주석) : https://www.acmicpc.net/problem/27294
# 간단한 문제 설명 : 
#   - 오전(0~11) 또는 저녁(17~23)이거나 술이 있으면 280개
#   - 점심(12~16)이고 술이 없으면 320개
# 시간/공간 복잡도 : O(1)

T, S = map(int, input().split(" "))

if S == 1 or (T <= 11 or T >= 17):
    print(280)
elif 12 <= T <= 16 and S == 0:
    print(320)