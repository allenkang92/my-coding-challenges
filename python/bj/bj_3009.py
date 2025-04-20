# 문제 링크 : https://www.acmicpc.net/problem/3009
# 간단한 문제 설명 : 
#   축에 평행한 직사각형의 세 점이 주어졌을 때, 네 번째 점을 찾는 문제입니다.
#
# 해결 방법 설명 : 
#   - 입력받은 세 점의 x, y 좌표를 각각 리스트에 저장합니다.
#   - 각 좌표에서 한 번만 등장하는 값이 네 번째 점의 좌표가 됩니다.
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(1)
#   - 공간 복잡도: O(1)

point_one = list(map(int, input().split()))
point_two = list(map(int, input().split()))
point_three = list(map(int, input().split()))

x_temp_list = []
x_temp_list.append(point_one[0])
x_temp_list.append(point_two[0])
x_temp_list.append(point_three[0])

y_temp_list = []
y_temp_list.append(point_one[1])
y_temp_list.append(point_two[1])
y_temp_list.append(point_three[1])

# 각 좌표에서 한 번만 등장하는 값 찾기
for x in x_temp_list:
    if x_temp_list.count(x) == 1:
        result_x = x

for y in y_temp_list:
    if y_temp_list.count(y) == 1:
        result_y = y

print(result_x, result_y)