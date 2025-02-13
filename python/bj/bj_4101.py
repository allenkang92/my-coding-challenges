# 문제 링크 (주석) : https://www.acmicpc.net/problem/4101
# 간단한 문제 설명 : 두 양의 정수가 주어졌을 때, 첫 번째 수가 두 번째 수보다 큰지 구하는 프로그램을 작성
# 해결 방법 설명 : while 루프를 사용하여 입력을 받고, a > b 조건을 확인하여 "Yes" 또는 "No"를 출력
# 시간/공간 복잡도 : O(N), N은 테스트 케이스의 수

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a > b:
        print("Yes")
    else:
        print("No")