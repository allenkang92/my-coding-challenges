# 문제 링크 (주석) : https://www.acmicpc.net/problem/25828
# 간단한 문제 설명 : 코로나 바이러스 검사 방법 중 개별 검사와 그룹 검사 중 어떤 방법이 더 적은 테스트 키트를 사용하는지 비교
# 해결 방법 설명 : 개별 검사와 그룹 검사에 필요한 키트 수를 계산하고, 두 방법을 비교
# 시간/공간 복잡도 : O(1) (입력 크기에 관계없이 일정한 시간과 공간이 소요됨)

# 입력 받기
g, p, t = map(int, input().split())

# 개별 검사 키트 수 계산
individual = g * p

# 그룹 검사 키트 수 계산
group = g + (t * p)

# 결과 비교 및 출력
if individual < group:
    print(1)
elif group < individual:
    print(2)
else:
    print(0)