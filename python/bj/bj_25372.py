# 문제 링크 : https://www.acmicpc.net/problem/25372
# 간단한 문제 설명 :
#   주어진 문자열이 현관문 비밀번호로 사용 가능한지 판별하는 문제입니다.
#   비밀번호 규칙은 비밀번호의 길이가 6자리 이상 9자리 이하여야 한다는 것입니다.
#
# 해결 방법 설명 :
#   문자열의 길이를 확인하여 6 이상 9 이하이면 "yes"를, 그렇지 않으면 "no"를 출력합니다.
#
# 시간/공간 복잡도 : O(N) (N은 입력된 문자열의 개수)

N = int(input())

for _ in range(N):
    pw = input()
    if 6 <= len(pw) <= 9:
        print("yes")
    else:
        print("no")