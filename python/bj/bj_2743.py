# 문제 링크 : https://www.acmicpc.net/problem/2743
# 간단한 문제 설명 : 
#   알파벳으로만 이루어진 단어를 입력받아
#   그 길이를 출력하는 프로그램
#
# 해결 방법 설명 : 
#   - 단어를 input()으로 입력받음
#   - len() 함수로 길이를 계산하여 출력
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(1) - 문자열 길이 계산
#   - 공간 복잡도: O(N) - N길이의 문자열 저장

word = input()

print(len(word))