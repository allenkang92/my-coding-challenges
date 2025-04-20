# 문제 링크 : https://www.acmicpc.net/problem/11948
# 간단한 문제 설명 : JOI가 선택한 과목의 총 점수를 계산하는 프로그램입니다.
# 해결 방법 설명 : 4과목 중 3과목을 선택하고, 역사와 지리 중 1과목을 선택하여 최대 점수를 계산합니다.
# 시간/공간 복잡도 : O(1)

A = int(input())  # 물리 점수 입력
B = int(input())  # 화학 점수 입력
C = int(input())  # 생물 점수 입력
D = int(input())  # 지구과학 점수 입력
E = int(input())  # 역사 점수 입력
F = int(input())  # 지리 점수 입력

# 자연 과학 점수를 정렬하여 리스트에 저장
nature_sci_score = sorted([A, B, C, D])
# 인문 과학 점수를 정렬하여 리스트에 저장
human_sci_score = sorted([E, F])

# 상위 3개 자연 과학 점수와 인문 과학 중 최대 점수를 합산
total_score = sum(nature_sci_score[1:]) + human_sci_score[-1]

# 최종 점수 출력
print(total_score)