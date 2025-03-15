# 문제 링크 (주석) : https://www.acmicpc.net/problem/32288
# 간단한 문제 설명 : 바코드 닉네임(소문자 'l'과 대문자 'I'로만 이루어진 문자열)의 모든 문자의 대소문자를 바꿔 출력
# 해결 방법 설명 : 문자열을 순회하며 'I'는 'i'로, 'l'은 'L'로 변환
# 시간/공간 복잡도 : O(n)

# 입력 처리: 바코드 닉네임의 길이 n과 문자열 S를 입력받음
n = int(input())
S = input()

# 변환된 문자열을 저장할 빈 문자열 초기화
change_S = str()

# 문자열 S를 순회하며 각 문자를 변환
for ch in S:
    if ch == 'I':
        change_S += 'i'  # 'I'를 'i'로 변환
    elif ch == 'l':
        change_S += 'L'  # 'l'을 'L'로 변환

# 결과 출력
print(change_S)