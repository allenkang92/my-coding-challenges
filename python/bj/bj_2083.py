# 문제 링크 (주석) : https://www.acmicpc.net/problem/2083
# 간단한 문제 설명 : 나이와 몸무게에 따라 회원을 Senior 또는 Junior로 분류
# 해결 방법 설명 : (age > 17 또는 weight >= 80)이면 Senior, 아니면 Junior
# 시간/공간 복잡도 : O(N)

while True:
    name, age, weight = input().split(" ")
    if name == "#" and age == "0" and weight == "0":
        break
    age = int(age)
    weight = int(weight)
    if age > 17 or weight >= 80:
        print(f"{name} Senior")
    else:
        print(f"{name} Junior")