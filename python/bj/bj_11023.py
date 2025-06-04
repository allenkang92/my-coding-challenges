# 문제 링크 : https://www.acmicpc.net/problem/11023
# 간단한 문제 설명 : 한 줄에 입력된 N개의 수의 합을 구하는 문제
# 해결 방법 설명 : 입력을 공백으로 분리하여 정수 리스트로 변환한 후 합을 계산
# 시간/공간 복잡도 : O(N), N은 입력된 수의 개수

# 공백으로 구분된 정수들을 입력받아 리스트로 변환
N_list = list(map(int, input().split(" ")))

# 리스트의 모든 요소 합 출력
print(sum(N_list))