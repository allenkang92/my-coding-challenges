# 문제 링크 (주석) : https://www.acmicpc.net/problem/14065
# 간단한 문제 설명 : 마일/갤런 단위의 연비를 리터/100km 단위로 변환하세요.
# 해결 방법 설명 : 공식 `리터/100km = 235.214583 / 마일/갤런`을 사용하여 변환합니다.
# 시간/공간 복잡도 : O(1)

# 입력 받기
miles_per_gallon = float(input())

# 리터/100km로 변환
liters_per_100km = 235.214583 / miles_per_gallon

# 결과 출력 (소수점 6자리까지)
print(f"{liters_per_100km:.6f}")