# 문제 링크 (주석) : https://www.acmicpc.net/problem/30087
# 간단한 문제 설명 : 세미나 이름을 입력받아 해당 세미나가 열리는 교실을 출력하는 문제
# 해결 방법 설명 : 딕셔너리를 사용하여 세미나 이름에 해당하는 교실을 찾아서 출력
# 시간/공간 복잡도 : O(N)

N = int(input())

class_list = {"Algorithm"	: "204",
            "DataAnalysis" : "207",
            "ArtificialIntelligence" : "302",
            "CyberSecurity" : "B101",
            "Network" : "303",
            "Startup" : "501",
            "TestStrategy" : "105" }


for _ in range(N):
    where = input()
    print(class_list[where])