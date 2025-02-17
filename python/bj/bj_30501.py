# 문제 링크 (주석) : https://www.acmicpc.net/problem/30501
# 문제 설명:
#   N명의 용의자 중, 이름에 "S"가 들어있는 사람을 찾는 문제입니다.
#   관우를 죽인 범인의 이름은 반드시 이름에 "S"가 포함되어 있습니다.
#   항상 답이 유일하게 존재함이 보장됩니다.
#
# 해결 방법 설명:
#   각 용의자의 이름을 순회하면서 "S"가 이름에 포함되어 있으면 해당 이름을 출력합니다.
#
# 시간/공간 복잡도 : O(N)

N = int(input())
for _ in range(N):
    suspect = input().strip()
    if 'S' in suspect:
        print(suspect)
        break