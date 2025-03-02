# 문제 링크 (주석) : https://www.acmicpc.net/problem/26768
# 간단한 문제 설명 : 
# 해결 방법 설명 :            
# 시간/공간 복잡도 : 

import sys
line = sys.stdin.readline().rstrip()

trans_line = ""
for ch in line:
    if ch == "a": 
        trans_line += "4"
    elif ch == "e": 
        trans_line += "3"
    elif ch == "i": 
        trans_line += "1"
    elif ch == "o": 
        trans_line += "0"
    elif ch == "s": 
        trans_line += "5"
    else:
        trans_line += ch
print(trans_line)