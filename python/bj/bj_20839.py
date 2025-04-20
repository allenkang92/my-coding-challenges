# 문제 링크 : https://www.acmicpc.net/problem/20839
# 간단한 문제 설명 : 학생이 충족한 A, C, E 기준에 따라 성적을 부여하는 문제
# 해결 방법 설명 : 각 성적의 조건을 확인하여 적절한 성적을 출력
# 시간/공간 복잡도 : O(1) (입력 크기에 관계없이 일정한 시간과 공간이 소요됨)

# 입력 받기
x, y, z = map(int, input().split())  # A, C, E 기준의 총 개수
x_prime, y_prime, z_prime = map(int, input().split())  # 학생이 충족한 A, C, E 기준의 개수

# 성적 결정
if x_prime == x and y_prime == y and z_prime == z:
    print('A')
elif y_prime == y and z_prime == z and x_prime >= x / 2:
    print('B')
elif y_prime == y and z_prime == z:
    print('C')
elif z_prime == z and y_prime >= y / 2:
    print('D')
else:
    print('E')