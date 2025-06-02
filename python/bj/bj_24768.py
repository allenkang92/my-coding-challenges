# 문제 링크 : https://www.acmicpc.net/problem/24768
# 간단한 문제 설명 : 빌이 가진 달콤한 꿀(x)과 신 꿀(y)의 개수에 따라 결과를 출력하는 문제
# 해결 방법 설명 : 각 줄마다 x, y를 입력받고 조건에 따라 다른 메시지를 출력. "0 0"이 입력되면 종료
# 시간/공간 복잡도 : O(n), n은 테스트 케이스의 수

while True:
    line = input()
    if line == "0 0":
        break
    
    x, y = map(int, line.split())
    
    # 조건 1: 13의 미신 - 전체 병의 개수가 13개면 더 이상 대화하지 않음
    if x + y == 13:
        print("Never speak again.")
    # 조건 2: 달콤한 꿀이 신 꿀보다 많으면 대회에 감
    elif x > y:
        print("To the convention.")
    # 조건 3: 달콤한 꿀과 신 꿀이 같으면 결정 못함
    elif x == y:
        print("Undecided.")
    # 조건 4: 신 꿀이 달콤한 꿀보다 많으면 뒤처짐
    elif x < y:
        print("Left beehind.")