# 문제 링크 : 해당 없음
# 문제 설명 :
#   Mina가 추천한 학생 수 n이 주어질 때, 각 추천당 10%의 할인 혜택을 받는다.
#   무료 과정을 듣기 위해서는 총 100%의 할인 혜택이 필요하므로,
#   무료로 수강할 수 있는 과목의 수는 n을 10으로 나눈 몫(n // 10)입니다.
#
# 해결 방법 설명 :
#   n // 10의 결과를 출력합니다.
#
# 시간/공간 복잡도 : O(1)

n = int(input())
print(n // 10)