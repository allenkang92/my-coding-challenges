# 문제 링크 : https://www.acmicpc.net/problem/8437
# 간단한 문제 설명 : 두 사람의 사과 개수 합과 차이가 주어졌을 때, 각 사람이 가진 사과 개수를 구하는 프로그램
# 해결 방법 설명 : Klaudia의 사과 개수 = (합 + 차이) / 2, Natalia의 사과 개수 = (합 - 차이) / 2
# 시간/공간 복잡도 : O(1)

apple = int(input()) 
more = int(input()) 

X = (apple + more) // 2
Y = (apple - more) // 2

print(X)
print(Y)