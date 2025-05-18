# 문제 링크 : https://www.acmicpc.net/problem/33810
# 간단한 문제 설명 : 주어진 문자열이 "SciComLove"와 비교하여 몇 개의 문자가 다른지 계산
# 해결 방법 설명 : 각 위치별로 문자열을 비교하여 다른 문자의 개수를 세기
# 시간/공간 복잡도 : O(1) - 문자열의 길이가 항상 10으로 고정되어 있음

# 원본 문자열 정의
original = "SciComLove"

# 입력 받기
modified = input().strip()

# 다른 문자 개수 계산
diff_count = 0
for i in range(len(original)):
    if original[i] != modified[i]:
        diff_count += 1

# 결과 출력
print(diff_count)