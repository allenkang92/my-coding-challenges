# 문제 링크 : https://www.acmicpc.net/problem/27889
# 간단한 문제 설명 :
#   주어진 학교의 약칭에 대해, 해당 학교의 정식 명칭을 출력하는 문제입니다.
#
# 해결 방법 설명 :
#   미리 학교 약칭과 정식 명칭을 매핑한 딕셔너리를 정의한 후, 
#   입력된 약칭을 키로 하여 대응하는 정식 명칭을 출력합니다.
#
# 시간/공간 복잡도 : O(1)

ch = input()

schools = {
    "NLCS": "North London Collegiate School", 
    "BHA": "Branksome Hall Asia",
    "KIS": "Korea International School", 
    "SJA": "St. Johnsbury Academy"
}

print(schools[ch])