# 문제 링크 : https://www.acmicpc.net/problem/27323  (예시 참고)
# 간단한 문제 설명 : 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력합니다.
# 해결 방법 설명 : 입력받은 n과 m에 대해 m번, n개의 별을 출력합니다.
# 시간/공간 복잡도 : O(n*m)

n, m = map(int, input().strip().split(' '))

for _ in range(m):
    print("*" * n)