# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181949
# 간단한 문제 설명 : 주어진 문자열의 각 알파벳에 대해 대문자는 소문자로, 소문자는 대문자로 변환하여 출력합니다.
# 해결 방법 설명 : 문자열의 각 문자를 순회하며 isupper()와 islower() 메서드로 대소문자를 판별한 후,
#                 lower()나 upper() 메서드를 사용해 변환합니다.
# 시간/공간 복잡도 : O(n) (문자열의 길이에 비례)

str = input()
answer = []
for ch in str:
    if ch.isupper() == True:
        answer.append(ch.lower())
    elif ch.islower() == True:
        answer.append(ch.upper())
print("".join(answer))