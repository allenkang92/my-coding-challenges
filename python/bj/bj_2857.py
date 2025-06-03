# 문제 링크 : https://www.acmicpc.net/problem/2857
# 간단한 문제 설명 : 5명의 요원 중 첩보원명에 'FBI'가 포함된 FBI 요원을 찾는 문제
# 해결 방법 설명 : 각 요원의 첩보원명을 입력받아 'FBI' 문자열이 포함되어 있는지 확인하고, 포함된 요원의 번호를 출력
# 시간/공간 복잡도 : O(1) - 입력이 항상 5개로 고정되어 있음

# 각 요원을 추적하기 위한 딕셔너리 초기화 (키: 요원 번호, 값: FBI 포함 여부)
agent_dict = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}

# 5명의 요원 정보 입력 받기
for i in range(5):
    # 요원의 첩보원명 입력
    agent = input()
    
    # 'FBI'가 첩보원명에 포함되어 있는지 확인
    if 'FBI' in agent:
        # FBI가 포함되어 있으면 해당 요원 번호에 1로 표시
        agent_dict[str(i+1)] = 1

# FBI 요원 목록 생성
fbi_agents = [agent_num for agent_num, is_fbi in agent_dict.items() if is_fbi == 1]

# 결과 출력
if fbi_agents:
    print(' '.join(fbi_agents))
else:
    print("HE GOT AWAY!")