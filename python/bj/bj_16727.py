# 문제 링크 : https://www.acmicpc.net/problem/16727
# 간단한 문제 설명 : 두 팀 간의 축구 결승전 결과를 계산하는 문제
# 해결 방법 설명 : 총점과 원정 다득점 규칙을 적용하여 승자를 결정하거나, 승부차기로 넘어가는지 판단
# 시간/공간 복잡도 : O(1) (입력 크기에 관계없이 일정한 시간과 공간이 소요됨)

# 입력 받기
p1, s1 = map(int, input().split())  # 첫 번째 경기: Persepolis(p1) vs Esteghlal(s1)
s2, p2 = map(int, input().split())  # 두 번째 경기: Esteghlal(s2) vs Persepolis(p2)

# 총점 계산
persepolis_total = p1 + p2  # Persepolis의 총점
esteghlal_total = s1 + s2   # Esteghlal의 총점

# 결과 판단
if persepolis_total > esteghlal_total:
    print('Persepolis')  # Persepolis가 총점에서 이긴 경우
elif persepolis_total < esteghlal_total:
    print('Esteghlal')   # Esteghlal이 총점에서 이긴 경우
else:
    # 원정 다득점 규칙 적용
    if p2 > s1:  # Persepolis의 원정 다득점이 더 많은 경우
        print('Persepolis')
    elif p2 < s1:  # Esteghlal의 원정 다득점이 더 많은 경우
        print('Esteghlal')
    else:
        print('Penalty')  # 승부차기로 넘어가는 경우