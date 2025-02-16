# 문제 링크 (주석) : https://www.acmicpc.net/problem/32458
# 간단한 문제 설명 :
#   주어진 양의 부동소수점을 내림(바닥 함수) 처리하여 정수 부분만을 출력한다.
#
# 해결 방법 설명 :
#   float로 입력받은 후, int()를 사용하여 내림 효과를 얻는다.
#
# 시간/공간 복잡도 : O(1)

x = float(input())
print(int(x))