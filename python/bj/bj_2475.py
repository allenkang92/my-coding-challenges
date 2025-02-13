# 문제 링크 (주석) : https://www.acmicpc.net/problem/2475
# 간단한 문제 설명 : 고유번호의 처음 5자리 숫자를 입력받아 검증수를 계산하여 출력
# 해결 방법 설명 : 각 숫자를 제곱한 수의 합을 10으로 나눈 나머지를 계산
# 시간/공간 복잡도 : O(1)

num_line = map(int, input().split())

agg = []
for i in num_line:
    agg.append(i ** 2)

print(sum(agg) % 10)