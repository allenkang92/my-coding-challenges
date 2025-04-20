# 문제 링크 : https://www.acmicpc.net/problem/26332
# 간단한 문제 설명 : 고객이 구매한 물건의 수와 물건 하나의 가격이 주어졌을 때, 할인을 적용한 총 비용을 계산
# 해결 방법 설명 : 물건을 1개만 구매하면 할인 없음, 2개 이상 구매하면 추가로 구매한 각 물건에 대해 $2 할인
# 시간/공간 복잡도 : O(n) (고객의 수에 비례하여 시간과 공간이 소요됨)

# 입력 받기
n = int(input())  # 고객의 수

# 각 고객에 대해 비용 계산
for _ in range(n):
    c, p = map(int, input().split())  # 구매한 물건의 수, 물건 하나의 가격
    
    # 총 비용 계산
    if c == 1:
        total_cost = c * p
    else:
        total_cost = p + (c - 1) * (p - 2)
    
    # 결과 출력
    print(c, p)
    print(total_cost)