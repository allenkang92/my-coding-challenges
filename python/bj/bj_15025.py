# 문제 링크 (주석) : https://www.acmicpc.net/problem/15025
# 문제 설명:
#   주어진 왼쪽(l)과 오른쪽(r)의 뿔(또는 가지)의 개수를 이용하여, 
#   다음과 같이 무스의 종류를 판정하는 문제입니다.
#     - 만약 l과 r이 모두 0이면 "Not a moose"를 출력합니다.
#     - 만약 l과 r이 같다면, 무스는 "Even"이고, 점수는 l + r 입니다.
#     - 만약 l과 r이 다르다면, 무스는 "Odd"이고, 점수는 2 × (더 큰 수) 입니다.
#
# 해결 방법 설명:
#   입력받은 두 정수 l, r에 대해,
#     1) l과 r이 모두 0이면 "Not a moose" 출력,
#     2) l과 r이 같으면 "Even (l+r)" 출력,
#     3) 그렇지 않으면 "Odd (max(l, r) * 2)" 출력합니다.
#
# 시간/공간 복잡도 : O(1)

l, r = map(int, input().split())

if l == 0 and r == 0:
    print("Not a moose")
elif l == r:
    print(f"Even {l + r}")
else:
    print(f"Odd {max(l, r) * 2}")