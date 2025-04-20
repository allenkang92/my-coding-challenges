# 문제 링크 : https://www.acmicpc.net/problem/30224
# 간단한 문제 설명 :
#   주어진 정수가 7을 포함하는지와 7로 나누어 떨어지는지를 판별하여,
#   아래 조건에 따라 0, 1, 2, 3 중 하나를 출력한다.
#     - 7을 포함하지 않고 7로 나누어 떨어지지 않으면 0
#     - 7을 포함하지 않고 7로 나누어 떨어지면 1
#     - 7을 포함하고 7로 나누어 떨어지지 않으면 2
#     - 7을 포함하고 7로 나누어 떨어지면 3
#
# 해결 방법 설명 :
#   정수를 문자열로 입력받아 '7'이 포함된 여부를 확인하고,
#   정수형으로 변환한 후 7의 배수 여부를 판단한다.
#
# 시간/공간 복잡도 : O(len(n)), 여기서 n은 입력된 숫자의 자릿수

s = input()
n = int(s)

# 숫자에 '7'이 포함되어 있는지 확인
contain7 = '7' in s

# 숫자가 7로 나누어 떨어지는지 확인
divisible7 = (n % 7 == 0)

if not contain7 and not divisible7:
    print(0)
elif not contain7 and divisible7:
    print(1)
elif contain7 and not divisible7:
    print(2)
elif contain7 and divisible7:
    print(3)