# 문제 링크 : https://www.acmicpc.net/problem/30658
# 간단한 문제 설명 : 
#   Eric(Erí)는 첫 번째 단계의 팀 순위가 두 번째 단계에서 역전된다고 가정한다.
#   각 테스트 케이스에 대해, 첫 단계 팀 순서의 역순으로 재배열된 두 번째 단계 팀 순서를 출력한다.
#
# 해결 방법 설명 :
#   1. n개의 팀 번호를 입력받는다.
#   2. 입력받은 순서의 역순으로 팀 번호를 재배열한다.
#   3. 재배열된 팀 순서를 출력하고 각 테스트 케이스 뒤에 "0"을 출력한다.
#            
# 시간/공간 복잡도 : O(N) - N은 팀의 수

while True:
    n = int(input())
    if n == 0:
        break
    
    teams = []
    for _ in range(n):
        teams.append(int(input()))
    
    # 역순으로 팀 출력
    result = [0] * n
    for i in range(n):
        result[n - 1 - i] = teams[i]
    
    for team in result:
        print(team)
    print(0)  # 각 테스트 케이스 뒤에 "0" 출력