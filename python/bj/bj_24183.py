# 문제 링크 (주석) : https://www.acmicpc.net/problem/24183
# 간단한 문제 설명 : 우편물의 총 무게를 계산하는 문제
# 해결 방법 설명 : 각 구성 요소의 면적에 단위 면적당 무게를 곱하여 총 무게를 계산
# 시간/공간 복잡도 : O(1) (입력 크기에 관계없이 일정한 시간과 공간이 소요됨)

# 입력 받기
w_envelope, w_poster, w_info = map(int, input().split())

# 면적 계산 (mm² 단위)
area_envelope = 229 * 324 * 2  # C4 봉투 (두 장)
area_poster = 297 * 420 * 2   # A3 포스터 (두 장)
area_info = 210 * 297         # A4 정보지 (한 장)

# mm²를 m²로 변환 (1m² = 1,000,000mm²)
area_envelope_m2 = area_envelope / 1_000_000
area_poster_m2 = area_poster / 1_000_000
area_info_m2 = area_info / 1_000_000

# 총 무게 계산
total_weight = (w_envelope * area_envelope_m2) + \
               (w_poster * area_poster_m2) + \
               (w_info * area_info_m2)

# 결과 출력 (소수점 6자리까지)
print(f"{total_weight:.6f}")