# 문제 링크 (주석) : https://www.acmicpc.net/problem/1157
# 간단한 문제 설명 : 주어진 단어에서 가장 많이 사용된 알파벳을 찾습니다.
# 해결 방법 설명 : 1. 입력 문자열을 대문자로 변환
#                2. 각 알파벳의 등장 횟수를 딕셔너리에 저장
#                3. 최대 등장 횟수를 가진 알파벳 찾기
# 시간/공간 복잡도 : O(n) (n은 문자열의 길이)

word = input().upper()  # 입력받은 문자열을 대문자로 변환
count_dict = {}        # 알파벳 등장 횟수를 저장할 딕셔너리

# 각 알파벳의 등장 횟수 계산
for char in word:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1

# 최대 등장 횟수를 가진 알파벳 찾기
max_count = max(count_dict.values())
max_chars = [char for char, count in count_dict.items() if count == max_count]

# 결과 출력
print('?' if len(max_chars) > 1 else max_chars[0])