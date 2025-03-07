# 문제 링크 (주석) : https://www.acmicpc.net/problem/31616
# 간단한 문제 설명 : 주어진 문자열이 모두 같은 문자로 이루어져 있는지 확인
# 해결 방법 설명 : 문자열의 첫 번째 문자를 기준으로 모든 문자가 같은지 확인
# 시간/공간 복잡도 : O(N) (N은 문자열의 길이)

# 입력 처리
N = int(input())
S = input()

# 모든 문자 동일 여부 확인
is_all_same = all(c == S[0] for c in S)

# 결과 출력
print("Yes" if is_all_same else "No")