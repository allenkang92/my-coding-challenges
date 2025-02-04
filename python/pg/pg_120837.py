# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120837
# 간단한 문제 설명 : 
#   개미 군단 문제
#   사냥감 체력(hp)에 맞춰 최소의 개미를 구성하려고 합니다.
#   장군개미는 5의 공격력을, 병정개미는 3의 공격력을, 일개미는 1의 공격력을 갖고 있습니다.
#
# 해결 방법 설명 : 
#   - 우선 장군개미를 최대한 많이 사용한 후 남은 체력을 계산합니다.
#   - 남은 체력에 대해 병정개미를 최대한 많이 사용한 후 남은 체력을 다시 계산합니다.
#   - 마지막으로 남은 체력은 일개미로 채웁니다.
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(1)
#   - 공간 복잡도: O(1)

def solution(hp):
    answer = 0            # 최소 병력 수를 저장할 변수
    residual = 0          # 남은 체력을 저장할 변수
    general = 5           # 장군개미의 공격력
    soldier = 3           # 병정개미의 공격력
    worker = 1            # 일개미의 공격력
    
    # 장군개미를 최대로 사용할 수 있는 개수를 구합니다.
    answer += hp // general
    # 장군개미로 처리한 후 남은 체력을 계산합니다.
    residual = hp - (hp // general) * general
    
    # 남은 체력에 대해 병정개미를 최대로 사용할 수 있는 개수를 구합니다.
    answer += residual // soldier
    # 병정개미로 처리한 후 남은 체력을 계산합니다.
    residual = residual - (residual // soldier) * soldier
    
    # 남은 체력은 일개미로 채웁니다.
    answer += residual // worker
    # 연산 후 남은 체력(특별한 처리 없이 0이 될 것임)
    residual = residual - (residual // worker) * worker
    
    return answer