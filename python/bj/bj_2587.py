# 문제 링크 : https://www.acmicpc.net/problem/2587
# 간단한 문제 설명 : 다섯 개의 자연수가 주어질 때 이들의 평균과 중앙값(대표값 2)를 구합니다.
# 해결 방법 설명 :
# 1. 5개의 자연수를 입력받아 정수로 변환합니다.
# 2. 입력 받은 숫자들을 리스트에 저장하고, 오름차순으로 정렬합니다.
# 3. 평균은 리스트의 합을 길이로 나눈 값입니다.
# 4. 중앙값은 오름차순 정렬된 리스트의 가운데 요소입니다.
# 시간/공간 복잡도 : O(n log n) (정렬에 의한 시간 복잡도)

line_one = int(input())
line_two = int(input())
line_three = int(input())
line_four = int(input())
line_five = int(input())

# 입력받은 5개의 자연수를 리스트로 만들고 오름차순 정렬합니다.
num_list = sorted([line_one, line_two, line_three, line_four, line_five])

# 평균을 계산하여 출력
print(int(sum(num_list) / len(num_list)))
# 중앙값은 정렬된 리스트의 가운데 요소 (인덱스 2, 0부터 시작하므로)
print(num_list[len(num_list) // 2])