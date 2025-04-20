# 문제 링크 : https://www.acmicpc.net/problem/17903
# 간단한 문제 설명 : 3-SAT 문제 인스턴스가 만족스러운지 판단하는 문제
# 해결 방법 설명 : 절의 개수가 8 이상인지 확인하여 판단
# 시간/공간 복잡도 : O(1) (입력 크기에 관계없이 일정한 시간과 공간이 소요됨)

# 입력 받기
m, n = map(int, input().split())

# 절 입력 받기 (사용하지 않음)
for _ in range(m):
    input()

# 판단 및 결과 출력
if m >= 8:
    print("satisfactory")
else:
    print("unsatisfactory")