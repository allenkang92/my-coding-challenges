# 문제 링크 (주석) : https://www.acmicpc.net/problem/21638
# 문제 설명:
#   MCHS (러시아 긴급 상황부)에서 기상청으로부터 오늘과 내일의 기상 정보를 전달받았습니다.
#   오늘의 기온 t1(℃)과 풍속 v1(m/s), 내일의 기온 t2(℃)과 풍속 v2(m/s)가 주어집니다.
#   아래의 우선 순위에 따라 시민들에게 SMS로 경보 메시지를 보내야 합니다.
#
#   1. 내일 기온이 0℃ 미만이고 풍속이 10 m/s 이상이면 폭풍우 경보 메시지를 보내야 합니다:
#      "A storm warning for tomorrow! Be careful and stay home if possible!"
#
#   2. 그렇지 않고 내일 기온이 오늘보다 낮으면 한파 경보 메시지를 보냅니다:
#      "MCHS warns! Low temperature is expected tomorrow."
#
#   3. 그렇지 않고 내일 풍속이 오늘보다 높으면 강풍 경보 메시지를 보냅니다:
#      "MCHS warns! Strong wind is expected tomorrow."
#
#   위 조건 중 어느 것도 만족하지 않으면 "No message"를 출력합니다.
#
# 해결 방법:
#   주어진 조건 순서대로 if-elif 문을 사용하여 메시지를 결정하고 출력합니다.
#
# 시간/공간 복잡도 : O(1)

t1, v1 = map(int, input().split(" "))
t2, v2 = map(int, input().split(" "))

if t2 < 0 and v2 >= 10:
    print("A storm warning for tomorrow! Be careful and stay home if possible!")
elif t1 > t2:
    print("MCHS warns! Low temperature is expected tomorrow.")
elif v1 < v2:
    print("MCHS warns! Strong wind is expected tomorrow.")
else:
    print("No message")