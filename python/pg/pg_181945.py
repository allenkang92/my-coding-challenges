# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181945
# 간단한 문제 설명 : 주어진 문자열 str의 각 문자를 세로로 한 줄씩 출력합니다.  
# 해결 방법 설명 : 문자열의 각 문자를 순회하며 print() 함수를 사용해 각각 새로운 줄에 출력합니다.
# 시간/공간 복잡도 : O(n) (문자열의 길이에 비례)

str = input()

for ch in str:
    print(ch)