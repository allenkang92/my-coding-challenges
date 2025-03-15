# 문제 링크 (주석) : https://www.acmicpc.net/problem/32710
# 간단한 문제 설명 : 주어진 수 N이 구구단표에 등장하는지 확인
# 해결 방법 설명 : 2단부터 9단까지의 구구단을 생성하고, N이 A, B, C 중 하나에 해당하는지 확인
# 시간/공간 복잡도 : O(1)

N = int(input())

# 구구단표에 등장하는 모든 숫자를 저장할 리스트
num_list = list()

# 2단부터 9단까지의 구구단을 생성
for i in range(2, 9 + 1):
    for j in range(1, 9 + 1):
        num_list.append(i)  # A (단수)
        num_list.append(j)  # B (곱해지는 수)
        num_list.append(i * j)  # C (결과값)

# 중복 제거를 위해 set으로 변환 후 다시 리스트로 변환
num_list = list(set(num_list))

# N이 구구단표에 등장하는지 확인
if N in num_list:
    print(1)
else:
    print(0)