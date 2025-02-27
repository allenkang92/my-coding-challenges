# 문제 링크 (주석) : https://www.acmicpc.net/problem/23795
# 간단한 문제 설명 : 윤성이가 도박판에서 잃은 돈의 총합을 계산하는 문제
# 해결 방법 설명 : 베팅한 금액을 누적하여 총합을 계산
# 시간/공간 복잡도 : O(n) (입력의 개수에 비례하는 시간과 공간이 소요됨)

# 총합 초기화
total = 0

# 입력 받기
while True:
    bet = int(input())
    if bet == -1:
        break
    total += bet

# 결과 출력
print(total)