# 문제 링크 (주석) : https://www.acmicpc.net/problem/28927
# 간단한 문제 설명 : 맥스와 멜이 시청한 트레일러, 드라마, 영화 시간을 비교하여 누가 더 많은 시간을 시청했는지 출력
# 해결 방법 설명 : 각자 시청한 시간을 계산 후 비교
# 시간/공간 복잡도 : O(1)

Max_list = list(map(int, input().split(" ")))
Mel_list = list(map(int, input().split(" ")))

agg_max = (Max_list[0] * 3) + (Max_list[1] * 20) + (Max_list[2] * 120)
agg_mel = (Mel_list[0] * 3) + (Mel_list[1] * 20) + (Mel_list[2] * 120)

if agg_max == agg_mel:
    print("Draw")

elif agg_max > agg_mel:
    print("Max")

else:
    print("Mel")