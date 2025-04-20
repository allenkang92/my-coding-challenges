# 문제 링크 : https://www.acmicpc.net/problem/28635
# 간단한 문제 설명 : 인디케이터가 m까지의 숫자를 순환적으로 표시할 때, 현재 숫자 a에서 원하는 숫자 b로 변경하기 위해 필요한 최소 버튼 클릭 횟수를 계산
# 해결 방법 설명 : a와 b의 관계에 따라 최소 클릭 횟수를 계산
# 시간/공간 복잡도 : O(1) (상수 시간과 공간이 소요됨)

# 입력 받기
m = int(input())
a = int(input())
b = int(input())

# 최소 클릭 횟수 계산
if a == b:
    result = 0
elif b > a:
    result = b - a
else:
    result = m - a + b

# 결과 출력
print(result)