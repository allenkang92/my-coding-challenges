# 문제 링크 : https://www.acmicpc.net/problem/10768
# 문제 설명:
#   사용자로부터 입력받은 월(M)과 일(D)에 따라,
#   날짜가 2월 18일 이전이면 "Before", 이후이면 "After", 
#   2월 18일이면 "Special"을 출력하는 문제입니다.
#
# 해결 방법 설명:
#   입력된 월이 2보다 작으면 무조건 "Before",
#   2보다 크면 "After"를 출력합니다.
#   월이 2인 경우, 일을 비교하여 18보다 작으면 "Before",
#   18이면 "Special", 18보다 크면 "After"를 출력합니다.
#
# 시간/공간 복잡도 : O(1)

M = int(input())
D = int(input())

if M < 2:
    print("Before")
elif M > 2:
    print("After")
else:  # M == 2
    if D < 18:
        print("Before")
    elif D == 18:
        print("Special")
    else:  # D > 18
        print("After")