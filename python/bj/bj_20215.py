# 문제 링크 (주석) : https://www.acmicpc.net/problem/20215
# 간단한 문제 설명 : 직사각형 모서리를 자르는 두 가지 방법의 절단 길이 차이를 계산하는 문제
# 해결 방법 설명 : 직사각형으로 자르는 길이와 대각선으로 자르는 길이를 계산하여 차이를 출력
# 시간/공간 복잡도 : O(1) (입력 크기에 관계없이 일정한 시간과 공간이 소요됨)

import math

# 입력 받기
w, h = map(int, input().split())

# 직사각형으로 자르는 길이
rectangle_cut = w + h

# 대각선으로 자르는 길이
diagonal_cut = math.sqrt(w**2 + h**2)

# 차이 계산
difference = rectangle_cut - diagonal_cut

# 결과 출력 (소수점 9자리까지 출력)
print(f"{difference:.9f}")