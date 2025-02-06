# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181849
# 간단한 문제 설명 : 한 자리 정수로 구성된 문자열 num_str의 각 자리 숫자를 모두 더한 값을 반환합니다.
# 해결 방법 설명 : 문자열의 각 문자를 순회하면서 정수로 변환 후 리스트에 저장하고, sum() 함수로 모든 값을 더합니다.
# 시간/공간 복잡도 : O(n)

def solution(num_str):
    # 각 자리 숫자를 저장할 리스트 생성
    num_list = []
    # 문자열의 각 문자(숫자)를 순회
    for i in num_str:
        # 문자를 정수로 변환 후 리스트에 추가
        num_list.append(int(i))
    # 리스트에 저장된 숫자들의 합을 반환
    return sum(num_list)