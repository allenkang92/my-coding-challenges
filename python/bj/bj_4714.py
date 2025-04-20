# 문제 링크 : https://www.acmicpc.net/problem/4714
# 간단한 문제 설명:
#   지구에서의 무게가 주어지면 달에서의 무게(지구 무게의 0.167배)를 계산하여,
#   "Objects weighing X on Earth will weigh Y on the moon." 형식으로 출력하는 문제입니다.
#
# 해결 방법 설명:
#   입력 값을 반복해서 받아, 음수가 들어오면 종료합니다.
#   각 입력에 대해, 달의 무게를 계산하고 소수점 둘째 자리까지 포맷하여 출력합니다.
#
while True:
    weight = float(input())
    if weight < 0:
        break
    moon_weight = weight * 0.167
    print(f"Objects weighing {weight:.2f} on Earth will weigh {moon_weight:.2f} on the moon.")