# 문제 링크 : https://www.acmicpc.net/problem/31520
# 간단한 문제 설명 : 주어진 숫자가 Champernowne 단어인지 확인하고, 몇 번째 단어인지 출력
# 해결 방법 설명 : 1부터 시작하여 숫자를 순서대로 이어붙여가며 주어진 숫자와 비교
# 시간/공간 복잡도 : O(k) (k는 Champernowne 단어의 길이)

# 입력 처리
n = input()

# Champernowne 단어 확인
champernowne = ''
k = 1
while len(champernowne) < len(n):
    champernowne += str(k)
    if champernowne == n:
        print(k)
        exit()
    k += 1

# 결과 출력 (Champernowne 단어가 아닌 경우)
print(-1)