# 문제 링크 : https://www.acmicpc.net/problem/32314
# 간단한 문제 설명 :
#   크리스마스 트리의 전류(a, ampere)와 후보 어댑터의 전력(w, watt) 및 전압(v, volt)이 주어진다.
#   어댑터의 전류는 (watt / volt)로 계산된다. 입력은 분수 없이 정확히 나누어 떨어진다고 가정한다.
#   어댑터의 전류가 트리의 전류보다 크거나 같으면 1, 그렇지 않으면 0을 출력한다.
#
# 해결 방법 설명 :
#   입력받은 w와 v로 어댑터의 전류를 계산한 후, 트리의 전류와 비교하여 조건에 따라 출력한다.
#
# 시간/공간 복잡도 : O(1)

a = int(input())
w, v = map(int, input().split())

# 정수 나눗셈을 사용해 어댑터의 전류를 계산 (분수 없이 정수로 계산됨)
adapter_ampere = w // v

if adapter_ampere >= a:
    print(1)
else:
    print(0)