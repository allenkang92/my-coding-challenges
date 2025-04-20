# 문제 링크 : https://www.acmicpc.net/problem/22193
# 간단한 문제 설명 :
#   N자리 정수 A, M자리 정수 B를 곱한 결과를 출력하는 문제
# 해결 방법 설명 :
#   - Python은 큰 정수를 기본적으로 처리 가능하므로 int 변환 후 곱셈 수행
#   - 출력 시 불필요한 0을 앞에 붙이지 않음
# 시간/공간 복잡도 : 크기가 최대 5만 자리이므로 처리 가능 (Python 무제한 정수)

N, M = map(int, input().split())
A = int(input())
B = int(input())

print(A * B)