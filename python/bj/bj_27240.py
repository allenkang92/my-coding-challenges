# 문제 링크 (주석) : https://www.acmicpc.net/problem/27240
# 간단한 문제 설명 : 전철 노선에서 출발역과 도착역에 따라 적용할 요금을 결정
# 해결 방법 설명 : 출발역과 도착역이 도시에 속하는지, 지역에 속하는지 확인하고, 요금을 결정
# 시간/공간 복잡도 : O(1) (상수 시간과 공간이 소요됨)

# 입력 받기
n, a, b = map(int, input().split())
s, t = map(int, input().split())

# 출발역과 도착역이 도시에 속하는지 확인
def is_city(station):
    return a < station < b

# 출발역과 도착역이 지역에 속하는지 확인
def is_outside(station):
    return station <= a or station >= b

# 요금 결정
if is_city(s) and is_city(t):
    print("City")
elif is_outside(s) and is_outside(t):
    if (s <= a and t <= a) or (s >= b and t >= b):
        print("Outside")
    else:
        print("Full")
else:
    print("Full")