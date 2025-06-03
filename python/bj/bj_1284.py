# 문제 링크 : https://www.acmicpc.net/problem/1284
# 간단한 문제 설명 : 주소판의 너비를 계산하는 문제. 각 숫자는 다른 너비를 가짐 (1:2cm, 0:4cm, 나머지:3cm)
# 해결 방법 설명 : 각 숫자의 너비를 더하고, 숫자 사이 여백(1cm)과 좌우 경계 여백(각 1cm)을 계산
# 시간/공간 복잡도 : O(n), n은 입력된 주소 숫자의 자릿수

# 테스트 케이스 반복 처리
while True:
    # 입력 받기
    N = input()
    
    # 종료 조건
    if N == '0':
        break
    
    # 좌우 경계 여백으로 시작 (1cm씩 총 2cm)
    result = 2
    
    # 각 숫자별 너비 계산
    for i in N:
        if i == '1':
            result += 2  # 1은 2cm 차지
        elif i == '0':
            result += 4  # 0은 4cm 차지
        else:
            result += 3  # 나머지 숫자는 모두 3cm 차지
    
    # 숫자 사이 여백 추가 (숫자 개수 - 1)
    result += len(N) - 1
    
    # 결과 출력
    print(result)