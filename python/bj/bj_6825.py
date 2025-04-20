# 문제 링크 : https://www.acmicpc.net/problem/6825
# 문제 설명:
#   BMI(Body Mass Index)를 계산하여, 해당되는 범주에 따라 메시지를 출력하는 문제입니다.
#   BMI = weight / (height ** 2)
#   - BMI > 25: "Overweight"
#   - 18.5 <= BMI <= 25.0: "Normal weight"
#   - BMI < 18.5: "Underweight"
#
# 해결 방법 설명:
#   입력받은 몸무게와 키를 이용하여 BMI를 계산하고,
#   조건문을 통해 해당 범주에 따른 결과를 출력합니다.
#
# 시간/공간 복잡도 : O(1)

w = float(input())
h = float(input())

BMI = w / (h ** 2)

if BMI > 25:
    print("Overweight")
elif 18.5 <= BMI <= 25.0:
    print("Normal weight")
else:
    print("Underweight")