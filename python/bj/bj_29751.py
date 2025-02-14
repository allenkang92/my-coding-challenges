# 문제 링크 (주석) : https://www.acmicpc.net/problem/29751
# 간단한 문제 설명 : 밑변 W, 높이 H인 삼각형의 넓이를 소수점 첫째 자리까지 출력
# 해결 방법 설명 : 삼각형 넓이 공식 (W * H) / 2 사용
# 시간/공간 복잡도 : O(1)

W, H = map(int, input().split(" "))

print(f"{(W * H) / 2:.1f}")