# 문제 링크 : https://www.acmicpc.net/problem/25932
# 문제 설명:
#   Dr. Orooji의 쌍둥이 맥(Mack, 저지 번호 18)과 잭(Zack, 저지 번호 17)이 축구를 합니다.
#   한 세트에 10개의 서로 다른 선수 저지 번호(11 ~ 99)가 주어집니다.
#   이 중에서 17과 18의 존재 여부를 확인하여 다음 메시지를 출력합니다.
#       - 17과 18 둘 다 있으면 "both"
#       - 17만 있으면 "zack"
#       - 18만 있으면 "mack"
#       - 둘 다 없으면 "none"
#
#   출력 형식은 각 테스트 케이스(세트)를 입력된 그대로 한 줄에 출력하고,
#   다음 줄에 해당 메시지를 출력한 후, 빈 줄을 추가합니다.
#
# 해결 방법:
#   각 테스트 케이스마다 정수 리스트를 입력받아,
#   17과 18의 존재 여부에 따라 조건문을 통해 메시지를 결정하고 출력합니다.
#
# 시간/공간 복잡도 : O(n), n은 테스트 케이스의 개수

n = int(input())
for _ in range(n):
    numbers = list(map(int, input().split()))
    # 입력된 숫자들을 그대로 출력
    print(*numbers)
    # 17과 18의 존재 여부에 따라 메시지 결정
    if 17 in numbers and 18 in numbers:
        print("both")
    elif 17 in numbers and 18 not in numbers:
        print("zack")
    elif 17 not in numbers and 18 in numbers:
        print("mack")
    else:
        print("none")
    # 각 테스트 케이스 후 빈 줄 출력
    print()