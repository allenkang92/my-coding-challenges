# 문제 링크 : https://www.acmicpc.net/problem/31614
# 간단한 문제 설명 :
#   주어진 정수 H (시간)와 M (분)을 입력받아, H시간 M분이 몇 분인지를 계산하여 출력한다.
#
# 해결 방법 설명 :
#   H를 분단위로 환산하기 위해 60을 곱한 후 M을 더하여 총 분을 계산한다.
#
# 시간/공간 복잡도 : O(1)

H = int(input())
M = int(input())

HtoM = H * 60
print(HtoM + M)