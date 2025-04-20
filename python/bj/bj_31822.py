# 문제 링크 : https://www.acmicpc.net/problem/31822
# 간단한 문제 설명 : 재수강할 과목의 과목 코드와 수강 신청 가능한 과목 목록이 주어졌을 때, 재수강으로 인정되는 과목의 개수를 출력
# 해결 방법 설명 : 과목 코드의 앞 5자리가 일치하는지 확인
# 시간/공간 복잡도 : O(N)

# 입력 처리
retake_code = input()
N = int(input())
count = 0
for _ in range(N):
    course_code = input()
    if retake_code[:5] == course_code[:5]:
        count += 1

# 결과 출력
print(count)