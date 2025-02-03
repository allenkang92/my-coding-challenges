# 문제 링크 (주석) : https://www.acmicpc.net/problem/1152
# 간단한 문제 설명 : 
#   영어 대소문자와 공백으로 이루어진 문자열에서
#   단어의 개수를 세는 프로그램
#
# 해결 방법 설명 : 
#   - input().strip()으로 문자열 입력받고 앞뒤 공백 제거
#   - split()으로 공백 기준 단어 분리
#   - len()으로 단어 개수 계산
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(N) - 문자열 길이에 비례
#   - 공간 복잡도: O(N) - 분리된 단어들 저장

letter = input().strip()

word_count = []
word_count = letter.split()

print(len(word_count))