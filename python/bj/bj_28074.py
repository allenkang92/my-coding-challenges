# 문제 링크 (주석) : https://www.acmicpc.net/problem/28074
# 간단한 문제 설명 : 주어진 문자열에서 'M', 'O', 'B', 'I', 'S'가 모두 포함되어 있는지 확인
# 해결 방법 설명 : 문자열에 필요한 모든 문자가 포함되어 있는지 확인
# 시간/공간 복잡도 : O(n) (n은 문자열의 길이)

# 입력 받기
s = input()

# 필요한 문자들
required = {'M', 'O', 'B', 'I', 'S'}

# 모든 문자가 포함되어 있는지 확인
if required.issubset(s):
    print("YES")
else:
    print("NO")