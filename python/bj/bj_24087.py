# 문제 링크 : https://www.acmicpc.net/problem/24087
# 간단한 문제 설명 : 높이가 S cm 이상인 아이스크림 타워를 구매하기 위한 최소 비용 구하기
# 해결 방법 설명 : 기본 아이스크림은 높이가 A cm이고 250엔, 추가 아이스크림은 개당 100엔에 높이가 B cm 증가함
#                 기본 아이스크림으로 시작해서 필요한 만큼의 추가 아이스크림을 구매하는 최소 비용 계산
# 시간/공간 복잡도 : O(1)

S = int(input())  # 원하는 높이(cm)
A = int(input())  # 기본 아이스크림 높이(cm)
B = int(input())  # 추가 아이스크림 1개당 증가하는 높이(cm)

# 기본 가격
cost = 250

# 기본 아이스크림만으로 충분한 경우
if A >= S:
    print(cost)
else:
    # 추가로 필요한 높이
    extra_height_needed = S - A
    
    # 필요한 추가 아이스크림 개수 (올림 나눗셈)
    extra_scoops = (extra_height_needed + B - 1) // B
    
    # 총 비용
    total_cost = cost + (extra_scoops * 100)
    
    print(total_cost)