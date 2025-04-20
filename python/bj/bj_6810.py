# 문제 링크 : https://www.acmicpc.net/problem/6810
# 간단한 문제 설명 : 주어진 13자리 ISBN 번호의 1-3 합계를 계산하는 프로그램입니다.
# 해결 방법 설명 : 첫 10자리 숫자와 입력받은 3자리 숫자를 이용하여 1-3 합계를 계산합니다.
# 시간/공간 복잡도 : O(1)

# 첫 10자리 ISBN
isbn_prefix = "9780921418"

# 마지막 3자리 입력 받기
last_three_digits = [int(input()) for _ in range(3)]

# 전체 ISBN 구성
isbn = isbn_prefix + ''.join(map(str, last_three_digits))

# 1-3 합계 계산
total_sum = 0
for i in range(13):
    if i % 2 == 0:  # 1의 자리
        total_sum += int(isbn[i]) * 1
    else:  # 3의 자리
        total_sum += int(isbn[i]) * 3

# 결과 출력
print(f"The 1-3-sum is {total_sum}")