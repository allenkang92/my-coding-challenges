# 문제 링크 : https://www.acmicpc.net/problem/15680
# 간단한 문제 설명 : N이 0이면 "YONSEI"를, 1이면 "Leading the Way to the Future"를 출력하는 프로그램
# 해결 방법 설명 : if-else 문을 사용하여 N 값에 따라 다른 문자열을 출력
# 시간/공간 복잡도 : O(1)

N = int(input())

if N == 0 :
    print("YONSEI")

else: 
    print("Leading the Way to the Future")