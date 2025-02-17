# 문제 링크 (주석) : https://www.acmicpc.net/problem/6841
# 문제 설명:
#   입력된 문자 단축어에 대해 대응하는 문장을 출력하는 프로그램입니다.
#   단축어가 번역 테이블에 있으면 번역된 결과를 출력하고,
#   그렇지 않으면 원래의 입력을 그대로 출력합니다.
#   단축어 "TTYL"이 입력되면 "talk to you later"를 출력한 후 프로그램을 종료합니다.
#
# 해결 방법 설명:
#   단축어에 대한 if-elif-else 조건문을 사용하여 대응하는 문자열을 출력합니다.
#
# 시간/공간 복잡도 : O(1) per input

while True:
    short_form = input()
    if short_form == "CU":
        print("see you")
    elif short_form == ":-)":
        print("I’m happy")
    elif short_form == ":-(":
        print("I’m unhappy")
    elif short_form == ";-)":
        print("wink")
    elif short_form == ":-P":
        print("stick out my tongue")
    elif short_form == "(~.~)":
        print("sleepy")
    elif short_form == "TA":
        print("totally awesome")
    elif short_form == "CCC":
        print("Canadian Computing Competition")
    elif short_form == "CUZ":
        print("because")
    elif short_form == "TY":
        print("thank-you")
    elif short_form == "YW":
        print("you’re welcome")
    elif short_form == "TTYL":
        print("talk to you later")
        break
    else: 
        print(short_form)