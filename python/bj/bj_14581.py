# 문제 링크 (주석) : https://www.acmicpc.net/problem/14581
# 간단한 문제 설명 : 홍준의 아이디를 입력받아 팬들에게 둘러싸인 홍준의 모습을 출력하는 프로그램
# 해결 방법 설명 : 주어진 형식에 맞춰 문자열을 출력
# 시간/공간 복잡도 : O(1)

ID = input()

print(":fan::fan::fan:")
print(f":fan::{ID}::fan:")
print(":fan::fan::fan:")