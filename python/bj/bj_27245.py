# 문제 링크 (주석) : https://www.acmicpc.net/problem/27245
# 간단한 문제 설명 : 방의 길이, 너비, 높이를 입력받아 방이 "좋은" 방인지 판단
# 해결 방법 설명 : 길이와 너비 중 작은 값과 높이의 비율이 2 이상이고, 큰 값과 작은 값의 비율이 2 이하인지 확인
# 시간/공간 복잡도 : O(1) (상수 시간과 공간이 소요됨)

# 입력 받기
w = int(input())
l = int(input())
h = int(input())

# 길이와 너비 중 작은 값과 큰 값 계산
min_side = min(w, l)
max_side = max(w, l)

# 조건 확인
if min_side / h >= 2 and max_side / min_side <= 2:
    print("good")
else:
    print("bad")