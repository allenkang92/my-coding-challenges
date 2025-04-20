# 문제 링크 : https://www.acmicpc.net/problem/28290
# 문제 설명:
#   입력된 8자리 문자열 S에 대해,
#   안밖 타법이면 "in-out",
#   밖안 타법이면 "out-in",
#   계단 타법이면 "stairs",
#   역계단 타법이면 "reverse"를 출력하고,
#   그 외의 경우 "molu"를 출력하는 문제입니다.

S = input()

if S == "fdsajkl;" or S == "jkl;fdsa":
    print("in-out")
elif S == "asdf;lkj" or S == ";lkjasdf":
    print("out-in")
elif S == "asdfjkl;":
    print("stairs")
elif S == ";lkjfdsa":
    print("reverse")
else:
    print("molu")