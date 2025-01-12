# 문제 링크 (주석) : https://www.acmicpc.net/problem/2588
# 간단한 문제 설명 : 
# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
# 해결 방법 설명 : 

# (1)의 위치에 들어갈 세 자리 자연수
one_line = int(input())

# (2)의 위치에 들어갈 세 자리 자연수
two_line = int(input())

# (3)의 위치에 들어갈 값
three_line = one_line * (two_line % 10)
print(three_line)

# (4)의 위치에 들어갈 값, //는 정수 나눗셈!
four_line = one_line * (two_line // 10 % 10)
print(four_line)

# (5)의 위치에 들어갈 값
five_line = one_line * (two_line // 100)
print(five_line)

# (6)의 위치에 들어갈 값
six_line = one_line * two_line
print(six_line)