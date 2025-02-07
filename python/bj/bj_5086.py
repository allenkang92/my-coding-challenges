# 문제 링크 (주석) : https://www.acmicpc.net/problem/5086
# 간단한 문제 설명 : 
#   - 두 수가 주어졌을 때, 첫 번째 숫자가 두 번째 숫자의 약수(factor)인지, 
#     첫 번째 숫자가 두 번째 숫자의 배수(multiple)인지, 둘 다 아닌지(neither)를 판별합니다.
# 해결 방법 설명 :
#   - F, S를 반복하여 입력받고, F==0 and S==0 이면 종료.
#   - F가 S로 나누어떨어지면 multiple, S가 F로 나누어떨어지면 factor, 둘 다 아니면 neither 출력.
# 시간/공간 복잡도 : 
#   - 나눗셈 연산은 상수 시간이므로, 입력받은 쌍의 수에 대해 O(1) 연산을 반복

while True:
    F, S = map(int, input().split())
    if F == 0 and S == 0:
        break
    
    if S != 0 and (F % S == 0):
        print("multiple")
    elif F != 0 and (S % F == 0):
        print("factor")
    else:
        print("neither")