# 문제 링크 : https://www.acmicpc.net/problem/2577
# 간단한 문제 설명 : 세 개의 자연수 A, B, C를 곱한 결과에 0~9 각 숫자가 몇 번 쓰였는지 세기
# 해결 방법 설명 :
# 1) A, B, C를 입력받아 곱한다.
# 2) 곱한 결과를 문자열로 변환하여 각 문자(숫자)를 순회하며 카운트 배열을 증가시킨다.
# 3) 0부터 9까지의 출현 횟수를 차례로 출력한다.
# 시간/공간 복잡도 : O(1)  (입력 크기가 고정되어 있어 상수 시간/공간)

A = int(input().strip())
B = int(input().strip())
C = int(input().strip())

# 곱셈 결과를 문자열로 변환
product_str = str(A * B * C)

# 0부터 9까지의 등장 횟수를 저장할 리스트
counts = [0] * 10

# 각 자리 숫자의 등장 횟수 세기
for ch in product_str:
    counts[int(ch)] += 1

# 결과 출력: 0~9 순서대로 한 줄에 하나씩
for cnt in counts:
    print(cnt)