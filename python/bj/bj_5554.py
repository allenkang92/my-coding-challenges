# 문제 링크 (주석) : https://www.acmicpc.net/problem/5554
# 문제 설명:
#   하루 동안 측정한 이동 시간이 초 단위로 주어질 때, 총 이동 시간을 몇 분 몇 초인지 계산하는 문제이다.
#
# 입력:
#   총 4줄에 걸쳐 각 이동 시간을 초 단위로 입력받는다.
#
# 출력:
#   첫 번째 줄에 이동시간의 분(x)을, 두 번째 줄에 초(y)를 출력한다.
#
# 해결 방법:
#   4개의 초를 모두 더한 후, 그 합을 60으로 나눈 몫과 나머지를 계산한다.
#
# 시간/공간 복잡도: O(1)

moving_time = 0
for _ in range(4):
    moving_time += int(input())

x = moving_time // 60
y = moving_time % 60

print(x)
print(y)