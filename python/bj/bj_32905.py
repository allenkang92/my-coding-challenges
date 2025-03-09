# 문제 링크 (주석) : https://www.acmicpc.net/problem/32905
# 간단한 문제 설명 : 
#   RACI 매트릭스가 올바르게 구성되었는지 확인하는 문제
#   RACI 매트릭스는 프로젝트 이해관계자들의 역할을 나타냄
#   - R (Responsible): 작업을 수행하는 사람 
#   - A (Accountable): 작업에 대한 최종 책임자, 각 작업(행)마다 정확히 1명만 존재해야 함
#   - C (Consulted): 작업 수행 중 자문을 제공하는 사람
#   - I (Informed): 작업 진행에 관한 정보를 받는 사람
#   - -: 관여 없음
#   
# 해결 방법 설명 :            
#   1. 각 행(작업)별로 'A'의 개수를 확인
#   2. 모든 행에 정확히 하나의 'A'가 있으면 "Yes" 출력, 그렇지 않으면 "No" 출력
#
# 시간/공간 복잡도 : O(n*m) - n은 행의 개수, m은 열의 개수

# 입력 처리
n, m = map(int, input().split())  # 행과 열의 개수

# RACI 매트릭스 유효성 검사
is_valid = True

for _ in range(n):
    row = input().split()
    
    # 각 행에 'A'의 개수 확인
    a_count = row.count("A")
    
    # 'A'가 정확히 1개가 아니라면 유효하지 않음
    if a_count != 1:
        is_valid = False
        break

# 결과 출력
print("Yes" if is_valid else "No")