# 문제 링크 (주석) : https://www.acmicpc.net/problem/3046
# 간단한 문제 설명 : R2가 몇 인지, R2를 잊었지만 R1과 S는 기억하고 있다. <<
# 해결 방법 설명 : 

R1, S = map(int, input().split(" "))

print(2 * S - R1)