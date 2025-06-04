# 문제 링크 : https://www.acmicpc.net/problem/10886
# 간단한 문제 설명 : N명의 사람들이 준희가 귀여운지 아닌지에 대한 설문조사 결과 처리
# 해결 방법 설명 : 1(귀여움)과 0(귀엽지 않음) 투표를 집계하여 과반수 의견을 출력            
# 시간/공간 복잡도 : O(N), N은 설문조사에 참여한 사람 수

# 설문조사에 참여한 사람 수 입력
N = int(input())

# 각 사람의 의견 수집
N_list = []
for _ in range(N):
    opinion = int(input())  # 0: 귀엽지 않음, 1: 귀여움
    N_list.append(opinion)

# 귀엽다는 의견(1)이 과반수인지 확인
if sum(N_list) > N / 2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")