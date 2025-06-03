# 문제 링크 : https://www.acmicpc.net/problem/2712
# 간단한 문제 설명 : 미터법과 미국 단위계 사이의 단위 변환 문제 (kg<->lb, l<->g)
# 해결 방법 설명 : 주어진 변환 비율을 사용하여 단위를 변환하고 결과를 소수점 4째자리까지 출력            
# 시간/공간 복잡도 : O(T), T는 테스트 케이스의 개수

# 테스트 케이스 개수 입력
T = int(input())

# 각 테스트 케이스 처리
for _ in range(T):
    # 값과 단위 입력
    N, unit = input().split(" ")
    N = float(N)
    
    # 단위에 따라 변환하고 출력
    if unit == "kg":
        # 킬로그램 -> 파운드 (1kg = 2.2046lb)
        print(f"{N * 2.2046:.4f} lb")
    elif unit == "lb":
        # 파운드 -> 킬로그램 (1lb = 0.4536kg)
        print(f"{N * 0.4536:.4f} kg")
    elif unit == 'g':
        # 갤런 -> 리터 (1g = 3.7854l)
        print(f"{N * 3.7854:.4f} l")
    elif unit == 'l':
        # 리터 -> 갤런 (1l = 0.2642g)
        print(f"{N * 0.2642:.4f} g")