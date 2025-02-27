# 문제 링크 (주석) : https://www.acmicpc.net/problem/17362
# 간단한 문제 설명 : 주어진 자연수 n에 해당하는 손가락 번호를 찾는 문제
# 해결 방법 설명 : n을 8로 나눈 나머지를 통해 손가락 번호를 결정
# 시간/공간 복잡도 : O(1) (입력 크기에 관계없이 일정한 시간과 공간이 소요됨)

# 입력 받기
n = int(input())

# 패턴 분석 및 결과 출력
remainder = n % 8
if remainder == 1:
    print(1)
elif remainder == 2:
    print(2)
elif remainder == 3:
    print(3)
elif remainder == 4:
    print(4)
elif remainder == 5:
    print(5)
elif remainder == 6:
    print(4)
elif remainder == 7:
    print(3)
else:  # remainder == 0
    print(2)