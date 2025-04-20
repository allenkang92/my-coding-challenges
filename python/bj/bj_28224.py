# 문제 링크 : https://www.acmicpc.net/problem/28224
# 간단한 문제 설명 : 특정 기간 동안 상품의 가격 변화를 계산하여 최종 가격을 구함
# 해결 방법 설명 : 초기 가격에 일별 가격 변화를 더하여 최종 가격을 계산
# 시간/공간 복잡도 : O(n) (n일에 비례하여 시간과 공간이 소요됨)

# 입력 받기
n = int(input())
price = int(input())

# 가격 계산
for _ in range(n - 1):
    change = int(input())
    price += change

# 결과 출력
print(price)