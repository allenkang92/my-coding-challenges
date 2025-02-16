# 문제 링크 (주석) : https://www.acmicpc.net/problem/23235
# 간단한 문제 설명 : 
#   첫 줄에 N과 N개의 정수가 주어지며 모두 비내림차순(sorted) 상태
#   N=0 이 들어오면 반복 종료
#   각 테스트 케이스마다 "Case X: Sorting... done!" 한 줄만 출력
# 시간/공간 복잡도 : O(1) (테스트마다 한 번의 출력)

case_num = 1
while True:
    line = input().strip()
    if not line:
        # 입력이 더 이상 없으면 종료
        break
    data = list(map(int, line.split()))
    N = data[0]
    if N == 0:
        break
    # 여기서 N개의 정수는 이미 정렬되어 있다고 가정 (문제 설명)
    # 테스트 케이스 당 결과 한 줄 출력
    print(f"Case {case_num}: Sorting... done!")
    case_num += 1