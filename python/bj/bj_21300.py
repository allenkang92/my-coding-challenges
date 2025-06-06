# 문제 링크 : https://www.acmicpc.net/problem/21300
# 간단한 문제 설명 :
#   미국의 음료수 용기 보증금 제도에 따라, 빈 용기의 갯수가 주어지면 고객이 환급받을 총 보증금(센트 단위)을
#   계산하는 문제.
# 해결 방법 설명 :
#   입력으로 주어진 6개의 정수(맥주, 맥아, 와인 제품, 탄산 음료, 셀처, 물 용기 빈 개수)의 합에 5를 곱한 값을 출력하면 된다.
# 시간/공간 복잡도 : O(1)

total_ins = map(int, input().split(" "))
print(sum(total_ins) * 5)