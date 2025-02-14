# 문제 링크 (주석) : https://codeup.kr/problem.php?id=6069
# 간단한 문제 설명 :
#   평가 문자(A, B, C, D 등)를 입력받아, 해당 평가에 대응하는 문자열을 출력하는 문제입니다.
#
# 해결 방법 설명 :
#   if-elif-else 구문을 사용하여 평가 문자가 A, B, C, D인지 확인하고,
#   그 외 문자들인 경우에는 "what?"을 출력합니다.
#
# 시간/공간 복잡도 : O(1)

ch = input()

if ch == "A":
    print("best!!!")
elif ch == "B":
    print("good!!")
elif ch == "C":
    print("run!")
elif ch == "D":
    print("slowly~")
else:
    print("what?")