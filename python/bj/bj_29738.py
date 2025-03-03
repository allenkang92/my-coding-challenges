# 문제 링크 (주석) : https://www.acmicpc.net/problem/29738
# 간단한 문제 설명 : Google Code Jam 참가자가 마지막으로 참가한 라운드를 등수에 따라 판단
# 해결 방법 설명 : 등수에 따라 라운드를 판단하고, 지정된 형식으로 출력
# 시간/공간 복잡도 : O(T) (테스트 케이스 수에 비례하여 시간과 공간이 소요됨)

# 입력 받기
T = int(input())

# 각 테스트 케이스에 대해 처리
for i in range(1, T + 1):
    N = int(input())
    
    # 라운드 판단
    if N <= 25:
        round = "World Finals"
    elif N <= 1000:
        round = "Round 3"
    elif N <= 4500:
        round = "Round 2"
    else:
        round = "Round 1"
    
    # 결과 출력
    print(f"Case #{i}: {round}")