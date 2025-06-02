# 문제 링크 : https://www.acmicpc.net/problem/33964
# 간단한 문제 설명 : X자리 레퓨닛과 Y자리 레퓨닛의 합을 구하는 문제
# 해결 방법 설명 : 문자열 반복을 통해 X자리와 Y자리 레퓨닛을 생성한 후 더하기
# 시간/공간 복잡도 : O(X+Y) - 레퓨닛 생성에 필요한 반복 횟수에 비례

# 입력 받기: X와 Y를 공백으로 구분하여 받음
X, Y = map(int, input().split(" "))

# X자리 레퓨닛 생성을 위한 빈 문자열 초기화
rep_x = ''
# Y자리 레퓨닛 생성을 위한 빈 문자열 초기화
rep_y = ''

# X번 반복하여 1을 추가해 X자리 레퓨닛 생성
for x in range(X):
    rep_x += '1'

# Y번 반복하여 1을 추가해 Y자리 레퓨닛 생성
for y in range(Y):
    rep_y += '1'

# 두 레퓨닛을 정수로 변환하여 더한 결과 출력
print(int(rep_x) + int(rep_y))