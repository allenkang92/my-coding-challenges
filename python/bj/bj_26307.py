# 문제 링크 : https://www.acmicpc.net/problem/26307
# 간단한 문제 설명 : 9:00 AM부터 HH:MM까지 흐른 시간을 분 단위로 계산
# 해결 방법 설명 : (HH - 9)시간을 분으로 변환하고, MM을 더함
# 시간/공간 복잡도 : O(1)

HH, MM = map(int, input().split(" "))

agg_HH = (HH - 9) * 60
agg_MM = MM

print(agg_HH + agg_MM)