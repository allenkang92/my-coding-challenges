# 문제 링크 : https://www.acmicpc.net/problem/28431
# 간단한 문제 설명 : 5개의 양말 중에서 짝을 이루지 못한 하나의 숫자를 찾음
# 해결 방법 설명 : 각 숫자의 등장 횟수를 카운트하고, 홀수인 숫자를 찾아 출력
# 시간/공간 복잡도 : O(1) (상수 시간과 공간이 소요됨)

# 입력 받기
socks = [int(input()) for _ in range(5)]

# 숫자 카운트
count = {}
for sock in socks:
    if sock in count:
        count[sock] += 1
    else:
        count[sock] = 1

# 짝을 이루지 못한 숫자 찾기
for key, value in count.items():
    if value % 2 == 1:
        print(key)
        break