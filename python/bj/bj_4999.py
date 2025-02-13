# 문제 링크 (주석) : https://www.acmicpc.net/problem/4999
# 간단한 문제 설명 : 재환이가 낼 수 있는 "aah"의 길이와 의사가 요구하는 길이가 주어졌을 때, 그 병원에 가야하는지 말아야하는지를 알아내는 프로그램을 작성
# 해결 방법 설명 : 재환이가 낼 수 있는 "aah"의 길이가 의사가 요구하는 길이보다 크거나 같으면 "go"를 출력하고, 그렇지 않으면 "no"를 출력
# 시간/공간 복잡도 : O(1)

j = input()
doc = input()

if len(j) >= len(doc):
    print("go")
else:
    print("no")