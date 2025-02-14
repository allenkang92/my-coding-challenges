# 문제 링크 (주석) : https://codeup.kr/problem.php?id=6070
# 간단한 문제 설명 :
#   월이 입력되면 해당하는 계절 이름을 출력하는 문제입니다.
#
# 해결 방법 설명 :
#   n을 3으로 나누어 몫이 1이면 "spring", 2이면 "summer", 3이면 "fall"로 출력,
#   그 외는 "winter"로 출력합니다. (1,2,12월은 winter, 3,4,5월은 spring, 6,7,8월은 summer, 9,10,11월은 fall)
#
# 시간/공간 복잡도 : O(1)

n = int(input())

if n // 3 == 1:
    print("spring")
elif n // 3 == 2:
    print("summer")
elif n // 3 == 3:
    print("fall")
else:
    print("winter")