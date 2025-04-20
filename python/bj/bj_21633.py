# 문제 링크 : https://www.acmicpc.net/problem/21633
# 간단한 문제 설명 : 은행 송금 수수료를 계산하는 문제
# 해결 방법 설명 : 기본 수수료와 추가 수수료를 합산하고, 최소/최대 수수료 범위를 적용
# 시간/공간 복잡도 : O(1) (입력 크기에 관계없이 일정한 시간과 공간이 소요됨)

# 입력 받기
k = int(input())

# 수수료 계산
commission = 25 + 0.01 * k
commission = max(commission, 100)  # 최소 수수료 적용
commission = min(commission, 2000)  # 최대 수수료 적용

# 결과 출력 (소수점 둘째 자리까지)
print(f"{commission:.2f}")