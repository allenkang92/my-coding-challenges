# 문제 링크 (주석) : https://www.acmicpc.net/problem/3052
# 간단한 문제 설명 : 
#   10개의 수를 입력받아 42로 나눈 나머지를 구하고
#   서로 다른 나머지가 몇 개인지 출력하는 프로그램
#
# 해결 방법 설명 : 
#   - 10개의 숫자를 한 줄씩 입력받음
#   - 각 숫자를 42로 나눈 나머지를 set에 추가
#   - set은 자동으로 중복을 제거
#   - set의 길이를 출력하여 서로 다른 나머지의 개수 확인
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(1) - 항상 10개의 숫자만 처리
#   - 공간 복잡도: O(1) - 최대 42개의 서로 다른 나머지만 저장 가능

remainders = set() 

for _ in range(10): 
    num = int(input())  
    remainders.add(num % 42)  

print(len(remainders))