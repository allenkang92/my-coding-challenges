# 문제 링크 (주석) : https://www.acmicpc.net/problem/16394
# 간단한 문제 설명 : 주어진 년도가 홍익대학교 개교 몇 주년인지 계산하는 프로그램
# 해결 방법 설명 : 입력받은 년도에서 개교 년도(1946)를 빼서 주년 계산
# 시간/공간 복잡도 : O(1)

N = int(input())
open_year = 1946

print(N - open_year)