# 문제 링크 (주석) : https://www.acmicpc.net/problem/10430
# 간단한 문제 설명 : (A+B)%C는 ((A%C) + (B%C))%C 와 같을까? 
#                (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
#                 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
# 해결 방법 설명 : A, B, C를 입력받은 후, 각각의 값을 출력한다.

A, B, C = map(int, input().split(" "))
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)

# print((A + B) % C == ((A % C) + (B % C)) % C)
# print((A * B) % C == ((A % C) * (B % C)) % C)