# 문제 링크 (주석) : https://www.acmicpc.net/problem/5596
# 문제 설명 :
#   민국이와 만세가 본 4과목(정보, 수학, 과학, 영어)의 점수를 입력받아,
#   민국이의 총점 S와 만세의 총점 T 중에서 큰 점수를 출력하는 문제입니다.
#   만약 두 총점이 같다면 민국이의 총점 S를 출력합니다.
#
# 해결 방법 설명 :
#   각 줄의 4개 점수를 정수로 입력받아 합계를 계산합니다.
#   두 합계 중에서 더 큰 값이 출력되며, 같을 경우 S(민국이의 총점)가 출력됩니다.
#
# 시간/공간 복잡도 : O(1)

MK = list(map(int, input().split()))
MS = list(map(int, input().split()))

sum_MK = sum(MK)
sum_MS = sum(MS)

if sum_MK >= sum_MS:
    print(sum_MK)
else:
    print(sum_MS)