# 문제 링크 : https://www.acmicpc.net/problem/18330
# 간단한 문제 설명 : Mahya가 다음 달에 사용할 휘발유의 양과 현재 남은 할당량을 바탕으로 다음 달 휘발유 비용을 계산하는 문제
# 해결 방법 설명 : 할당량 내에서는 리터당 1500 Oshloobs, 할당량을 초과하면 리터당 3000 Oshloobs를 지불
# 시간/공간 복잡도 : O(1) (입력 크기에 관계없이 일정한 시간과 공간이 소요됨)

# 입력 받기
n = int(input())  # 다음 달에 사용할 휘발유 양
k = int(input())  # 현재 남은 할당량

# 다음 달의 총 할당량 계산
total_quota = k + 60

# 비용 계산
if n <= total_quota:
    cost = n * 1500  # 할당량 내에서 사용
else:
    cost = total_quota * 1500 + (n - total_quota) * 3000  # 할당량 초과

# 결과 출력
print(cost)