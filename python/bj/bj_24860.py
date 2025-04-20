# 문제 링크 : https://www.acmicpc.net/problem/24860
# 간단한 문제 설명 : 주어진 유전자 조각 변이의 수를 기반으로 가능한 항체(Immunoglobulin) 분자의 총 수를 계산
# 해결 방법 설명 : 각 경쇄와 중쇄의 조합 수를 계산하고, 이를 곱하여 총 항체 조합 수를 구함
# 시간/공간 복잡도 : O(1) (입력 크기에 관계없이 일정한 시간과 공간이 소요됨)

# 입력 받기
V_kappa, J_kappa = map(int, input().split())  # κ-경쇄의 V와 J 변이 수
V_lambda, J_lambda = map(int, input().split())  # λ-경쇄의 V와 J 변이 수
V_h, D_h, J_h = map(int, input().split())  # 중쇄의 V, D, J 변이 수

# 경쇄 조합 수 계산
light_chain = V_kappa * J_kappa + V_lambda * J_lambda

# 중쇄 조합 수 계산
heavy_chain = V_h * D_h * J_h

# 총 항체 조합 수 계산
total_antibodies = light_chain * heavy_chain

# 결과 출력
print(total_antibodies)