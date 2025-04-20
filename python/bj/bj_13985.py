# 문제 링크 : https://www.acmicpc.net/problem/13985
# 간단한 문제 설명 : "a + b = c" 형식의 산술 퀴즈가 주어졌을 때, 답이 맞는지 확인하세요.
# 해결 방법 설명 : 입력 문자열을 '='를 '=='로 바꾸고, eval 함수를 사용하여 결과를 판단합니다.
# 시간/공간 복잡도 : O(1)

# 입력 받기
inputs = input()

# '='를 '=='로 바꾸기
inputs = inputs.replace("=", "==")

# 결과 판단 및 출력
if eval(inputs) == True:
    print("YES")
else:
    print("NO")