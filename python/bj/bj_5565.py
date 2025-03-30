# 문제 링크 : https://www.acmicpc.net/problem/5565
# 간단한 문제 설명 : 10권의 책 중 9권의 가격이 주어졌을 때, 나머지 1권의 가격을 구하는 문제
# 해결 방법 설명 : 총 가격에서 9권의 가격을 빼면 나머지 1권의 가격을 구할 수 있음
# 시간/공간 복잡도 : O(1)

# 총 가격 입력
total_price = int(input())

# 9권의 가격을 더할 식별자 초기화
sum_of_nine = 0

# 9권의 가격 입력 및 합계 계산
for _ in range(9):
    sum_of_nine += int(input())

# 나머지 1권의 가격 계산
remaining_price = total_price - sum_of_nine

# 결과 출력
print(remaining_price)