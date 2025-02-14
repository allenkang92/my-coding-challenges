# 문제 링크 (주석) : https://www.acmicpc.net/problem/28235
# 간단한 문제 설명 : 주어진 구호에 따라 정해진 응원 문구를 출력하는 프로그램
# 해결 방법 설명 : if-elif-else 구문을 사용하여 입력된 구호에 맞는 응원 문구를 출력
# 시간/공간 복잡도 : O(1)

say = input()

if say == "SONGDO":
    print("HIGHSCHOOL")
elif say == "CODE":
    print("MASTER")
elif say == "2023":
    print("0611")
elif say == "ALGORITHM":
    print("CONTEST")