# 문제 링크 (주석) : https://www.acmicpc.net/problem/31612
# 간단한 문제 설명 : 주어진 문자열에서 각 문자의 획수를 계산하여 총 획수를 구함
# 해결 방법 설명 : 각 문자의 획수를 계산하여 총 획수를 구함
# 시간/공간 복잡도 : O(N) (N은 문자열의 길이)

# 입력 처리
N = int(input())
S = input()

# 획수 계산
stroke_count = 0
for char in S:
    if char == 'j':
        stroke_count += 2
    elif char == 'o':
        stroke_count += 1
    elif char == 'i':
        stroke_count += 2

# 결과 출력
print(stroke_count)