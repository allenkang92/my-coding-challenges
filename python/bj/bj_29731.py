# 문제 링크 (주석) : https://www.acmicpc.net/problem/29731
# 간단한 문제 설명 :
#   주어진 N개의 문장이 Rick Astley의 원래 공약에 속하는지 확인하는 문제입니다.
#   하나라도 공약에 속하지 않는 문장이 있으면 "Yes", 모두 속하면 "No"를 출력합니다.
#
# 해결 방법 설명 :
#   미리 Rick Astley의 공약을 담은 리스트를 정의한 후, 입력된 각 문장이 이 리스트에 포함되는지 확인합니다.
#
# 시간/공간 복잡도 : O(N)

N = int(input())
S = []
for _ in range(N):
    S.append(input())

# Rick Astley의 원래 공약들을 미리 정의 (반복문 밖에서 한 번만 정의합니다)
Astley = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop"
]

# 입력된 문장 중 하나라도 Astley에 없는 것이 있으면 변경된 것으로 판단합니다.
changed = False
for sentence in S:
    if sentence not in Astley:
        changed = True
        break

if changed:
    print("Yes")
else:
    print("No")