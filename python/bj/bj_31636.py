# 문제 링크 : https://www.acmicpc.net/problem/31636
# 간단한 문제 설명 : 주어진 문자열에서 'o'가 연속으로 3번 나오는 부분이 있는지 확인
# 해결 방법 설명 : 문자열을 순회하면서 'o'가 연속으로 3번 나오는 부분이 있는지 확인
# 시간/공간 복잡도 : O(N) (N은 문자열의 길이)

# 입력 처리
N = int(input())
S = input()

# 연속된 'o' 확인
has_three_o = False
for i in range(N - 2):
    if S[i] == S[i+1] == S[i+2] == 'o':
        has_three_o = True
        break

# 결과 출력
print("Yes" if has_three_o else "No")