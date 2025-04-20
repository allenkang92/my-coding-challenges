# 문제 링크 : https://www.acmicpc.net/problem/28940
# 간단한 문제 설명 : 주어진 페이지 크기와 글자 크기를 바탕으로, 모든 글자를 수용하기 위해 필요한 페이지 수를 계산
# 해결 방법 설명 : 한 페이지에 들어갈 수 있는 글자의 수를 계산하고, 필요한 페이지 수를 계산
# 시간/공간 복잡도 : O(1) (상수 시간과 공간이 소요됨)

# 입력 받기
w, h = map(int, input().split())
n, a, b = map(int, input().split())

# 한 페이지에 들어갈 수 있는 글자의 수 계산
letters_per_page = (w // a) * (h // b)

# 필요한 페이지 수 계산
if letters_per_page == 0:
    result = -1
else:
    result = (n + letters_per_page - 1) // letters_per_page

# 결과 출력
print(result)