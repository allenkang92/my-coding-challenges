# 문제 링크 : https://www.acmicpc.net/problem/6888
# 간단한 문제 설명 : 모든 직책이 바뀌는 연도를 찾는 프로그램입니다.
# 해결 방법 설명 : 주어진 연도 X에서 시작하여 60년 간격으로 연도를 찾아 출력합니다.
# 시간/공간 복잡도 : O(n)

X = int(input())
Y = int(input())

# 모든 직책이 바뀌는 연도는 60년 간격으로 발생
for year in range(X, Y + 1):
    if (year - X) % 60 == 0:
        print(f"All positions change in year {year}")