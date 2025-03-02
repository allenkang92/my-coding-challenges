# 문제 링크 (주석) : https://www.acmicpc.net/problem/26340
# 간단한 문제 설명 : 주어진 직사각형 종이를 특정 횟수만큼 접었을 때의 최종 크기를 계산
# 해결 방법 설명 : 종이를 접을 때는 항상 더 긴 변을 따라 접고, 홀수 길이의 변은 반올림하지 않고 버림
# 시간/공간 복잡도 : O(n * k) (테스트 케이스 수와 각 테스트 케이스의 접는 횟수에 비례하여 시간과 공간이 소요됨)

# 테스트 케이스 수 입력
n = int(input())

# 각 테스트 케이스 처리
for _ in range(n):
    # 종이의 두 변의 길이와 접는 횟수 입력
    a, b, folds = map(int, input().split())
    
    # "Data set: v" 출력
    print(f"Data set: {a} {b} {folds}")
    
    # 종이 접기
    for _ in range(folds):
        if a > b:
            a = a // 2
        else:
            b = b // 2
    
    # 최종 종이 크기 출력 (더 긴 변을 먼저 출력)
    print(max(a, b), min(a, b))
    
    # 테스트 케이스 사이에 빈 줄 추가
    print()