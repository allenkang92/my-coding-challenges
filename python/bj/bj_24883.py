# 문제 링크 (주석) : https://www.acmicpc.net/problem/24883
# 간단한 문제 설명 : 주어진 알파벳이 N 또는 n이면 "Naver D2", 아니라면 "Naver Whale"를 출력하는 문제
# 해결 방법 설명 : 
#   알파벳 한 문자를 입력받아, 'N' 또는 'n'이면 "Naver D2"를 출력하고, 그렇지 않으면 "Naver Whale"을 출력한다.
# 시간/공간 복잡도 : O(1)

alpha = input()

if alpha == 'N' or alpha == 'n':
    print("Naver D2")
else:
    print("Naver Whale")