# 문제 링크 (주석) : https://www.acmicpc.net/problem/14652
# 간단한 문제 설명 : 관중석 번호 K에 해당하는 좌표 (n, m)를 찾으세요.
# 해결 방법 설명 : K를 가로 길이 M으로 나누어 행(n)을 구하고, 나머지를 열(m)로 구합니다.
# 시간/공간 복잡도 : O(1)

# 입력 받기
N, M, K = map(int, input().split())

# 좌표 계산
n = K // M  # 행
m = K % M   # 열

# 결과 출력
print(n, m)