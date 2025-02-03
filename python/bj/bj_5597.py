# 문제 링크 (주석) : https://www.acmicpc.net/problem/5597
# 간단한 문제 설명 : 
#   30명의 학생 중 과제를 제출하지 않은 2명의 학생 번호를 찾는 프로그램
#   입력은 28줄로 각 제출자의 출석번호가 주어짐 (중복 없음)
#
# 해결 방법 설명 : 
#   - 1부터 30까지의 전체 학생 번호를 담은 set 생성
#   - 28명의 제출자 번호를 입력받아 set에서 제거
#   - 남은 2개의 번호를 정렬하여 한 줄씩 출력
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(1) - 항상 28번의 입력 처리
#   - 공간 복잡도: O(1) - 최대 30개의 번호만 저장

student_num = set(range(1, 31))

for _ in range(28):
    student_num.remove(int(input()))

no_show = sorted(list(student_num))
print(no_show[0])  # 가장 작은 번호 출력
print(no_show[1])  # 두 번째로 작은 번호 출력