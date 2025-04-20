# 문제 링크 : https://www.acmicpc.net/problem/4470
# 간단한 문제 설명 :
#   텍스트에서 줄을 입력받은 뒤, 각 줄의 앞에 줄 번호를 붙여 출력하는 프로그램입니다.
#
# 해결 방법 설명 :
#   첫 번째 줄에 주어진 정수 N만큼 반복하며, 각 줄을 읽은 후 해당 줄 번호와 함께 출력합니다.
#
# 시간/공간 복잡도 : O(N)

N = int(input())
for i in range(1, N + 1):
    line = input()
    print(f"{i}. {line}")