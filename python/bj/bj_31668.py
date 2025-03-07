# 문제 링크 (주석) : https://www.acmicpc.net/problem/31668
# 간단한 문제 설명 : 파묻튀밥에 들어가는 파묻튀를 가지로 바꿔치기하기 위해 필요한 가지의 양을 계산
# 해결 방법 설명 : 파묻튀밥의 줄 수를 계산하고, 이를 바탕으로 필요한 가지의 양을 계산
# 시간/공간 복잡도 : O(1) (상수 시간과 공간이 소요됨)

# 입력 처리
N = int(input())
M = int(input())
K = int(input())

# 필요한 가지의 양 계산
total_eggplant = (M // N) * K

# 결과 출력
print(total_eggplant)