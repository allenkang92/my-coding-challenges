# 문제 링크 (주석) : https://www.acmicpc.net/problem/26489
# 간단한 문제 설명 : 데이터 파일(입력)의 총 라인 수를 세어 출력
# 해결 방법 설명 : EOF가 발생할 때까지 한 줄씩 입력받아 개수를 누적
# 시간/공간 복잡도 : O(N) (N은 전체 라인 수)

count_lines = 0
while True:
    try:
        input()  # 한 줄 입력
        count_lines += 1
    except EOFError:
        break  # 입력이 더 이상 없으면 종료

print(count_lines)