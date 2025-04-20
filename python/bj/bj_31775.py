# 문제 링크 : https://www.acmicpc.net/problem/31775
# 문제 설명:
#   포닉스가 정한 응원 문구가 GLOBAL하기 위해서는,
#   주어진 3개의 문자열이 순서와 관계없이 각각 'l', 'k', 'p'로 시작해야 한다.
#   즉, 세 문자열의 첫 문자를 집합으로 만들었을 때, 그 집합이 {'l', 'k', 'p'}와 같아야 한다.
#
# 입력:
#   첫 번째 줄부터 3개의 줄에 걸쳐 문자열 S1, S2, S3가 주어진다.
#   모든 문자열은 알파벳 소문자 또는 숫자로 이루어진 길이 20 이하의 문자열이다.
#
# 출력:
#   응원 문구가 GLOBAL하면 "GLOBAL"을, 그렇지 않으면 "PONIX"를 출력한다.
#
# 해결 방법:
#   각 문자열의 첫 문자를 추출한 후, 그 집합이 {'l','k','p'}와 동일한지 비교한다.
#
# 시간/공간 복잡도 : O(1)

s1 = input().strip()
s2 = input().strip()
s3 = input().strip()

first_letters = {s1[0], s2[0], s3[0]}

if first_letters == {'l', 'k', 'p'}:
    print("GLOBAL")
else:
    print("PONIX")