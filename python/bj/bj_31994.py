# 문제 링크 (주석) : https://www.acmicpc.net/problem/31994
# 간단한 문제 설명 : 7개의 세미나 중 가장 많은 신청자 수를 가진 세미나의 이름을 출력
# 해결 방법 설명 : 각 세미나의 신청자 수를 비교하여 최대값을 찾음
# 시간/공간 복잡도 : O(1)

# 입력 처리
seminars = []
for _ in range(7):
    name, count = input().split()
    seminars.append((name, int(count)))

# 최대 신청자 수 찾기
max_seminar = max(seminars, key=lambda x: x[1])

# 결과 출력
print(max_seminar[0])