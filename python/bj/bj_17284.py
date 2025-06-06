# 문제 링크 : https://www.acmicpc.net/problem/17284
# 간단한 문제 설명 : 자판기에서 버튼을 누른 후 거스름돈을 계산하는 문제
# 해결 방법 설명 : 초기 금액 5000원에서 누른 버튼에 따라 음료수 가격을 차감
# 시간/공간 복잡도 : O(N), N은 버튼을 누른 횟수

# 공백으로 구분된 버튼 입력값 받기
button = list(input().split(" "))

# 초기 금액 5000원 설정
change = 5000

# 각 버튼 입력에 따라 금액 차감
for ch in button:
    if ch == "1":
        change -= 500    # 1번 버튼: 레쓰비 500원
    elif ch == "2":
        change -= 800    # 2번 버튼: 게토레이 800원
    elif ch == "3":
        change -= 1000   # 3번 버튼: 코카콜라 1000원

# 최종 거스름돈 출력        
print(change)