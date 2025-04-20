# 문제 링크 : https://www.acmicpc.net/problem/30664
# 간단한 문제 설명 :
#   각 테스트 케이스마다 주어지는 숫자(최대 30자리)가 42의 배수인지 판별한다.
#   만약 42의 배수라면 "PREMIADO"를 출력하고, 그렇지 않다면 "TENTE NOVAMENTE"를 출력한다.
#   입력은 0이 입력될 때까지 계속되며, 0은 처리하지 않는다.
#
# 해결 방법 설명 :
#   파이썬의 int 자료형은 임의 정밀도를 지원하므로, 큰 수에 대해 % 연산을 사용할 수 있다.
#   입력받은 수가 "0"이면 종료하고, 그렇지 않으면 42로 나눈 나머지를 확인한다.
#
# 시간/공간 복잡도 : O(k) (여기서 k는 입력 숫자의 자릿수)

while True:
    n = input().strip()
    if n == "0":
        break
    if int(n) % 42 == 0:
        print("PREMIADO")
    else:
        print("TENTE NOVAMENTE")