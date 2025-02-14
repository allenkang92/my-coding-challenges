# 문제 링크 (주석) : https://codeup.kr/problem.php?id=6067
# 간단한 문제 설명 :
#   음수/양수와 짝수/홀수를 판단하여 다음과 같이 분류해 출력합니다.
#   - 음수이면서 짝수: A
#   - 음수이면서 홀수: B
#   - 양수이면서 짝수: C
#   - 양수이면서 홀수: D
#
# 해결 방법 설명 :
#   숫자가 음수인지 양수인지, 또 짝수인지 홀수인지 조건문을 중첩하거나 논리연산자를 이용해 판단합니다.
#
# 시간/공간 복잡도 : O(1)

n = int(input())

if n < 0 and n % 2 == 0:
    print("A")
elif n < 0 and n % 2 != 0:
    print("B")
elif n > 0 and n % 2 == 0:
    print("C")
elif n > 0 and n % 2 != 0:
    print("D")