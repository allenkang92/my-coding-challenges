# 문제 링크 (주석) : https://www.acmicpc.net/problem/20976
# 문제 설명:
#   세 개의 정수 A, B, C가 주어질 때, 이들 중 두 번째로 큰 수를 출력하는 문제입니다.
#
# 해결 방법:
#   입력받은 세 정수를 리스트에 저장한 후 정렬하여, 
#   리스트의 중앙에 위치한 값을 출력합니다.
#
# 시간/공간 복잡도 : O(N) (여기서는 상수 시간)
A, B, C = map(int, input().split(" "))

abc_list = [A, B, C]
abc_list = sorted(abc_list)

print(abc_list[len(abc_list) // 2])