# 문제 링크 : https://codeup.kr/problem.php?id=6066
# 간단한 문제 설명 :
#   3개의 정수(a, b, c)가 입력되었을 때, 각각이 짝(even) 혹은 홀(odd)인지 출력합니다.
#
# 해결 방법 설명 :
#   각 정수를 순회하며 2로 나누어 나머지가 0이면 "even", 0이 아니면 "odd"를 출력합니다.
#
# 시간/공간 복잡도 : O(1)

a, b, c = map(int, input().split(" "))
num_list = [a, b, c]

for i in num_list:
    if i % 2 == 0:
        print("even")
    else:
        print("odd")