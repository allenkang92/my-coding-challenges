# 문제 링크 (주석) : https://www.acmicpc.net/problem/9506
# 간단한 문제 설명 : 주어진 수가 완전수인지 판단하고, 완전수라면 약수들의 합으로 표현합니다.
# 해결 방법 설명 : 1. 1부터 n-1까지 순회하며 약수들을 찾습니다.
#                2. 약수들의 합이 n과 같으면 완전수입니다.
#                3. 완전수인 경우 약수들을 오름차순으로 출력합니다.
# 시간/공간 복잡도 : O(n) (n까지의 약수를 찾는 과정)

while True:
    n = int(input())
    if n == -1:
        break
        
    divisors = []  # 약수를 저장할 리스트
    
    # 약수 찾기 (자기 자신 제외)
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
            
    # 완전수 판단
    if sum(divisors) == n:
        print(f"{n} = {' + '.join(map(str, divisors))}")
    else:
        print(f"{n} is NOT perfect.")