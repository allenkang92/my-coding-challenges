# 문제 링크 : https://www.acmicpc.net/problem/2920
# 간단한 문제 설명 : 주어진 8개 음의 순서가 ascending(1~8), descending(8~1) 또는 mixed인지 판별
# 해결 방법 설명 : 입력된 음의 순서와 미리 정의된 ascending, descending 순서를 비교하여 판별
# 시간/공간 복잡도 : O(1) - 입력과 비교하는 배열의 크기가 고정(8개)되어 있음

# 입력: 8개의 정수를 공백으로 구분하여 입력받음
line = list(map(int, input().split()))

# ascending(1~8) 순서인지 확인
if line == list(range(1, 9)):
    print("ascending")
# descending(8~1) 순서인지 확인
elif line == list(range(8, 0, -1)):
    print("descending")
# 둘 다 아니면 mixed
else:
    print("mixed")