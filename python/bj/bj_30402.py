# 문제 링크 (주석) : https://www.acmicpc.net/problem/30402
# 간단한 문제 설명 : 
#   15x15 픽셀로 이루어진 사진이 주어졌을 때, 특정 색상의 존재 여부를 통해 어떤 고양이의 사진인지 판별
#   - 하얀색(w)이 존재하면 춘배
#   - 검은색(b)이 존재하면 나비
#   - 회색(g)이 존재하면 영철
#   각 사진에는 고양이가 1마리만 등장함
# 
# 해결 방법 설명 :            
#   15x15 크기의 사진에서 각 픽셀을 확인하며 'w', 'b', 'g' 중 어떤 색상이 나타나는지 확인
#   발견된 색상에 따라 어떤 고양이인지 판별
# 
# 시간/공간 복잡도 : O(1) - 입력 크기가 고정됨 (15x15)

# 고양이 판별용 변수
has_white = False  # 춘배 (w)
has_black = False  # 나비 (b)
has_gray = False   # 영철 (g)

# 15x15 픽셀 확인
for _ in range(15):
    pixels = input().split()
    for pixel in pixels:
        if pixel == 'w':
            has_white = True
        elif pixel == 'b':
            has_black = True
        elif pixel == 'g':
            has_gray = True

# 결과 출력
if has_white:
    print("chunbae")
elif has_black:
    print("nabi")
elif has_gray:
    print("yeongcheol")