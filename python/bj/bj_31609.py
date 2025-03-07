# 문제 링크 (주석) : https://www.acmicpc.net/problem/31609
# 간단한 문제 설명 : 주어진 배열에서 적어도 한 번 이상 나타나는 숫자를 오름차순으로 출력
# 해결 방법 설명 : 중복된 숫자를 제거하고 오름차순으로 정렬하여 출력
# 시간/공간 복잡도 : O(N log N) (N은 배열의 길이)

# 입력 처리
N = int(input())
A = list(map(int, input().split()))

# 중복 제거 및 정렬
unique_numbers = sorted(set(A))

# 결과 출력
for num in unique_numbers:
    print(num)