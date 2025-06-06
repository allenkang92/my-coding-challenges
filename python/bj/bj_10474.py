# 문제 링크 : https://www.acmicpc.net/problem/10474
# 간단한 문제 설명 : 가분수(분자가 분모보다 크거나 같은 분수)를 대분수(정수부+진분수)로 변환하는 문제
# 해결 방법 설명 : 정수 나눗셈(몫)으로 정수부를 구하고, 나머지를 분자로 하여 대분수 표현
# 시간/공간 복잡도 : O(N), N은 입력으로 주어지는 분수의 개수

# 0 0이 입력될 때까지 반복
while True:
    # 분자와 분모 입력받기
    a, b = map(int, input().split(" "))
    
    # 종료 조건 검사
    if a == 0 and b == 0:
        break
        
    # 정수부 계산 (몫)
    int_part = a // b
    
    # 분수부의 분자 계산 (나머지)
    remainder = a - (int_part * b)
    
    # 대분수 형식으로 출력
    print(f"{int_part} {remainder} / {b}")