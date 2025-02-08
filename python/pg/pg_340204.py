# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/340204
# 간단한 문제 설명 : 환자 코드의 마지막 4글자를 확인하여 해당하는 병과를 출력합니다.
# 해결 방법 설명 : 문자열의 슬라이싱을 사용하여 마지막 4글자를 추출하고,
#                조건문으로 각 병과에 해당하는 경우를 처리합니다.
# 시간/공간 복잡도 : O(1) (문자열 슬라이싱과 단순 조건문)

code = input()
last_four_words = code[-4:]      # 마지막 4글자 추출

if last_four_words == "_eye":    # 안과
    print("Ophthalmologyc")
elif last_four_words == "head":  # 신경외과
    print("Neurosurgery")
elif last_four_words == "infl":  # 정형외과
    print("Orthopedics")
elif last_four_words == "skin":  # 피부과
    print("Dermatology")
else:                           # 그 외 경우
    print("direct recommendation")