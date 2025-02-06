# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120843
# 간단한 문제 설명 : 
#   공을 한 명 건너뛰고 던질 때, k번째로 공을 받는 사람의 번호를 구합니다.
#
# 해결 방법 설명 : 
#   - k번째 던지기에서 공을 받는 사람의 인덱스는 (k-1)*2 입니다.
#   - 인덱스가 numbers의 길이를 넘어가면 나머지 연산으로 순환시킵니다.
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(1)
#   - 공간 복잡도: O(1)

def solution(numbers, k):
    # k-1번째 던지기까지 이동한 후의 인덱스 계산
    # 한 번 던질 때마다 2칸씩 이동하므로 (k-1)*2
    return numbers[((k-1)*2) % len(numbers)]