# 문제 링크 (주석) : https://www.acmicpc.net/problem/26350
# 간단한 문제 설명 : 주어진 동전 단위가 특정 조건을 만족하는지 확인
# 해결 방법 설명 : 각 동전 단위가 이전 단위의 최소 두 배 이상인지 확인
# 시간/공간 복잡도 : O(n * d) (테스트 케이스 수와 각 테스트 케이스의 동전 단위 수에 비례하여 시간과 공간이 소요됨)

# 테스트 케이스 수 입력
n = int(input())

# 각 테스트 케이스 처리
for _ in range(n):
    # 동전 단위 입력
    denominations = list(map(int, input().split()))
    d = denominations[0]
    coins = denominations[1:]
    
    # "Denominations: v" 출력
    print(f"Denominations: {' '.join(map(str, coins))}")
    
    # 조건 확인
    is_good = True
    for i in range(1, d):
        if coins[i] < 2 * coins[i - 1]:
            is_good = False
            break
    
    # 결과 출력
    if is_good:
        print("Good coin denominations!")
    else:
        print("Bad coin denominations!")
    
    # 테스트 케이스 사이에 빈 줄 추가
    print()