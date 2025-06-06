# 문제 링크 : https://www.acmicpc.net/problem/26068
# 간단한 문제 설명 : 임스가 받은 치킨 기프티콘 중 유효기간이 90일 이하로 남은 기프티콘의 개수를 계산
# 해결 방법 설명 : 각 기프티콘의 남은 유효기간이 90일 이하인지 확인
# 시간/공간 복잡도 : O(n) (기프티콘의 개수에 비례하여 시간과 공간이 소요됨)

# 기프티콘의 개수 입력
N = int(input())

# 유효기간이 90일 이하인 기프티콘의 개수 초기화
count = 0

# 각 기프티콘의 유효기간 확인
for _ in range(N):
    # 유효기간 입력 (예: "D-86")
    x = input().strip()
    # "D-"를 제거하고 정수로 변환
    days = int(x[2:])
    # 유효기간이 90일 이하인지 확인
    if days <= 90:
        count += 1

# 결과 출력
print(count)