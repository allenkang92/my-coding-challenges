# 문제 링크 : https://www.acmicpc.net/problem/26768
# 간단한 문제 설명 : 주어진 문자열을 해커 슬랭으로 변환
# 해결 방법 설명 : 특정 문자를 해당하는 숫자로 변환
# 시간/공간 복잡도 : O(n) (문자열의 길이에 비례하여 시간과 공간이 소요됨)

# 입력 받기
text = input().strip()

# 문자 변환 규칙 정의
conversion = {
    'a': '4',
    'e': '3',
    'i': '1',
    'o': '0',
    's': '5'
}

# 변환된 문자열 생성
hacker_text = ''.join([conversion.get(char, char) for char in text])

# 결과 출력
print(hacker_text)