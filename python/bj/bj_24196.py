# 문제 링크 : https://www.acmicpc.net/problem/24196
# 간단한 문제 설명 : 암호화된 문자열을 복호화하는 문제
# 해결 방법 설명 : 첫 번째 문자를 시작으로, 각 문자의 알파벳 순서에 따라 다음 문자의 위치를 결정하여 복호화
# 시간/공간 복잡도 : O(n) (문자열의 길이에 비례하는 시간과 공간이 소요됨)

# 입력 받기
encrypted = input().strip()

# 복호화된 문자열 초기화
decrypted = ""

# 현재 위치 초기화
index = 0

# 복호화 과정
while index < len(encrypted):
    # 현재 문자를 복호화된 문자열에 추가
    decrypted += encrypted[index]
    # 다음 문자의 위치 계산 (A=1, B=2, ..., Z=26)
    next_step = ord(encrypted[index]) - ord('A') + 1
    # 다음 위치로 이동
    index += next_step

# 결과 출력
print(decrypted)