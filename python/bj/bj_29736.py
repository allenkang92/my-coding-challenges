# 문제 링크 : https://www.acmicpc.net/problem/29736
# 문제 설명:
#   부대원의 문제 푼 개수가 A, A+1, ..., B로 주어진다.
#   브실이가 푼 문제 수가 K일 때, 
#   본인과 푼 문제 수의 차이가 X 이하면 친구가 될 수 있다고 본다.
#   친구가 될 수 있는 사람의 수를 구하되, 한 명도 없다면 "IMPOSSIBLE"을 출력한다.
#
# 해결 방법 설명:
#   A부터 B까지 순회하면서, abs(K - i)가 X보다 작거나 같으면 친구 자격이다.
#   전체 친구 수를 세어 출력한다.
#
# 시간/공간 복잡도 : O(B-A)

A, B = map(int, input().split(" "))
K, X = map(int, input().split(" "))

friend_count = 0
for i in range(A, B+1):  # B도 포함해야 함
    if abs(K - i) <= X:
        friend_count += 1

if friend_count > 0:
    print(friend_count)
else:
    print("IMPOSSIBLE")