# 문제 링크 : https://www.acmicpc.net/problem/18408
# 문제 설명:
#   3개의 정수 A, B, C가 주어진다.
#   각 정수는 1 또는 2로만 이루어져 있으며, 1과 2 중 어느 쪽이 더 많이 등장하는지 판단하는 문제이다.
#
# 해결 방법:
#   입력받은 3개의 정수를 리스트에 저장한 후, count() 함수를 이용해 1과 2가 각각 몇 개 있는지 센다.
#   그리고 1의 개수가 2의 개수보다 많으면 1을, 그렇지 않으면 2를 출력한다.
#
# 시간/공간 복잡도 : O(1)

A, B, C = map(int, input().split(" "))
count_list = [A, B, C]

if count_list.count(1) > count_list.count(2):
    print(1)
elif count_list.count(1) < count_list.count(2):
    print(2)