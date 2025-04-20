# 문제 링크 : https://www.acmicpc.net/problem/23825
# 간단한 문제 설명 : SASA 모형을 만들기 위해 필요한 S 블록과 A 블록의 개수를 고려하여 최대 모형 개수를 계산
# 해결 방법 설명 : S 블록과 A 블록으로 만들 수 있는 모형 개수 중 작은 값을 선택
# 시간/공간 복잡도 : O(1) (입력 크기에 관계없이 일정한 시간과 공간이 소요됨)

# 입력 받기
N, M = map(int, input().split())

# 최대 SASA 모형 개수 계산
max_models = min(N // 2, M // 2)

# 결과 출력
print(max_models)