# 문제 링크 (주석) : https://www.acmicpc.net/problem/5622
# 간단한 문제 설명 : 
#   알파벳 대문자로 이루어진 단어를 다이얼로 걸 때 걸리는 시간 계산
#   각 숫자를 걸기 위해서는 기본 2초 + 추가 시간이 필요
#
# 해결 방법 설명 : 
#   - 입력받은 단어를 리스트로 변환
#   - 각 문자별로 다이얼 번호에 따른 시간 계산
#   - 모든 시간을 합산하여 출력
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(N) - 문자열 길이만큼 반복
#   - 공간 복간도: O(N) - 문자열 길이만큼 리스트 사용

word = input()
word_list = []
to_time = []

for i in word:
    word_list.append(i)

for j in word_list:
    if j in ["A", "B", "C"]:
        to_time.append(3)
    elif j in ["D", "E", "F"]:
        to_time.append(4)
    elif j in ["G", "H", "I"]:
        to_time.append(5)
    elif j in ["J", "K", "L"]:
        to_time.append(6)
    elif j in ["M", "N", "O"]:
        to_time.append(7)
    elif j in ["P", "Q", "R", "S"]:
        to_time.append(8)
    elif j in ["T", "U", "V"]:
        to_time.append(9)
    elif j in ["W", "X", "Y", "Z"]:
        to_time.append(10)

print(sum(to_time))