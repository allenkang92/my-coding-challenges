# 문제 링크 : https://www.acmicpc.net/problem/5988
# 간단한 문제 설명 : 주어진 숫자가 홀수인지 짝수인지 판별하는 문제
# 해결 방법 설명 : 입력된 수의 마지막 자리만 확인하면 홀짝 여부를 알 수 있음            
# 시간/공간 복잡도 : O(1) - 각 수의 마지막 자리만 확인

N = int(input())

for _ in range(N):
    num = int(input())
    if num % 2 == 0:
        print("even")
    else:
        print("odd")