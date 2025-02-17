# 문제 링크 (주석) : https://www.acmicpc.net/problem/5300
# 문제 설명:
#   N명의 해적에게 1부터 N까지 번호를 매긴 후,
#   6명마다 "Go!"를 출력하는 문제입니다.
#   마지막 그룹에 해적이 6명 미만인 경우에도 마지막에 "Go!"를 출력합니다.
#
# 해결 방법 설명:
#   1부터 N까지 순회하면서 번호를 문자열 리스트에 추가합니다.
#   각 번호가 6의 배수이면 "Go!"를 리스트에 추가하고,
#   순회가 끝난 후 마지막 번호가 6의 배수가 아니라면 "Go!"를 추가합니다.
#   리스트를 공백으로 조인하여 출력합니다.
#
# 시간/공간 복잡도 : O(N)

N = int(input().strip())
out_list = []

for i in range(1, N + 1):
    out_list.append(str(i))
    if i % 6 == 0:
        out_list.append("Go!")

if N % 6 != 0:
    out_list.append("Go!")

print(" ".join(out_list))