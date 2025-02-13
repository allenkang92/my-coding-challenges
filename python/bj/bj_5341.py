# 문제 링크 (주석) : https://www.acmicpc.net/problem/5341
# 간단한 문제 설명 : 밑변이 n인 피라미드를 만드는 데 필요한 총 블록 수를 계산하는 프로그램
# 해결 방법 설명 : 1부터 n까지의 합을 구하는 공식 이용 (n * (n + 1) // 2)
# 시간/공간 복잡도 : O(1)

while True:
    n = int(input())
    if n == 0:
        break
    
    num = n * (n + 1) // 2

    print(num)