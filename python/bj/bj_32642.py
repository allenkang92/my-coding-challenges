# 문제 링크 (주석) : https://www.acmicpc.net/problem/32642
# 간단한 문제 설명 : N일 동안의 날씨 정보를 기반으로 동우의 분노의 합을 계산
# 해결 방법 설명 : 비가 오는 날에는 분노를 1 증가, 비가 오지 않는 날에는 분노를 1 감소
# 시간/공간 복잡도 : O(N)

# 입력 처리
import sys  # 빠른 입력을 위해 sys 모듈 사용
input = sys.stdin.readline  # input 함수를 sys.stdin.readline으로 대체

N = int(input())  # N일 동안의 날씨 정보를 입력받음
weather = list(map(int, input().split()))  # N일 동안의 날씨 정보를 리스트로 저장

# 분노의 합 계산
anger = 0  # 현재 분노 상태를 저장할 변수 초기화
result = 0  # 분노의 누적 합을 저장할 변수 초기화
for day in weather:  # 날씨 정보를 순회
    if day == 1:  # 비가 오는 날
        anger += 1  # 분노 1 증가
    else:  # 비가 오지 않는 날
        anger -= 1  # 분노 1 감소
    result += anger  # 현재 분노를 누적 합에 더함

# 결과 출력
print(result)  # 분노의 누적 합 출력