# 문제 링크 : https://www.acmicpc.net/problem/32089
# 간단한 문제 설명 : n년 동안의 각 해의 신입 부원 수를 기반으로, 부원 수가 최대가 되는 해의 부원 수를 계산
# 해결 방법 설명 : 각 해의 부원 수는 해당 해와 그 전 2년의 신입 부원 수의 합으로 계산
# 시간/공간 복잡도 : O(n)

# 입력 처리
while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    
    # 최대 부원 수 계산
    max_members = 0
    for i in range(n):
        current_members = a[i]
        if i >= 1:
            current_members += a[i - 1]
        if i >= 2:
            current_members += a[i - 2]
        if current_members > max_members:
            max_members = current_members
    
    # 결과 출력
    print(max_members)