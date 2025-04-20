# 문제 링크 : https://www.acmicpc.net/problem/27918
# 간단한 문제 설명 : 달구와 포닉스가 탁구 경기를 진행할 때, 각 라운드의 승자를 예측하고 최종 점수를 계산
# 해결 방법 설명 : 각 라운드의 승자에 따라 점수를 업데이트하고, 누군가가 2점 앞서면 경기를 종료
# 시간/공간 복잡도 : O(N) (N회의 라운드에 비례하여 시간과 공간이 소요됨)

# 입력 받기
N = int(input())
results = [input().strip() for _ in range(N)]

# 점수 초기화
D_score = 0
P_score = 0

# 점수 계산
for result in results:
    if result == 'D':
        D_score += 1
    else:
        P_score += 1
    
    # 누군가가 2점 앞서면 경기 종료
    if abs(D_score - P_score) >= 2:
        break

# 결과 출력
print(f"{D_score}:{P_score}")