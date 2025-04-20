# 문제 링크 : https://www.acmicpc.net/problem/24083
# 간단한 문제 설명 : 아날로그 시계의 시침이 현재 가리키는 눈금 A에서 B시간 후에 가리키는 눈금을 계산
# 해결 방법 설명 : (A + B) % 12를 계산하고, 결과가 0이면 12를 출력
# 시간/공간 복잡도 : O(1) (입력 크기에 관계없이 일정한 시간과 공간이 소요됨)

# 입력 받기
A = int(input())
B = int(input())

# B시간 후 시침이 가리키는 눈금 계산
result = (A + B) % 12
if result == 0:
    print(12)
else:
    print(result)