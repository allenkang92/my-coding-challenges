# 문제 링크 : https://www.acmicpc.net/problem/33701
# 간단한 문제 설명 : 새천년관의 새로운 이름을 지어주는 문제. 이름은 1) 알파벳 소문자로만 구성, 2) 첫 글자와 마지막 글자가 같음, 3) k와 u 포함, 4) 마지막 4글자는 gwan, 5) 길이 50 이하여야 함
# 해결 방법 설명 : 마지막 4글자가 gwan이므로 마지막 글자는 n. 따라서 첫 글자도 n이어야 함. 중간 부분은 랜덤 생성하되 k와 u가 포함되도록 함. 정규표현식으로 최종 검증.            
# 시간/공간 복잡도 : O(1) - 길이가 최대 50으로 제한되어 있어 상수 시간 및 공간 복잡도를 가짐

import re
import random
import string

def generate_building_name():
    # 조건 1: 알파벳 소문자로만 이루어져야 함
    # 조건 2: 맨 앞 글자와 맨 뒤 글자는 같은 글자여야 함 (마지막 글자는 'n')
    # 조건 3: 알파벳 k와 u가 포함되어 있어야 함
    # 조건 4: 마지막 4글자는 gwan이어야 함
    # 조건 5: 길이가 50보다 짧거나 같아야 함
    
    # 마지막 글자가 'n'이므로 첫 글자도 'n'이어야 함
    first_letter = 'n'
    
    # 중간 부분 생성 (k와 u를 포함)
    middle_length = random.randint(1, 45)  # 총 길이 50 이하 (n + middle + gwan)
    middle_chars = random.choices(string.ascii_lowercase, k=middle_length)
    
    # k와 u가 포함되도록 함
    if 'k' not in middle_chars:
        middle_chars[random.randint(0, middle_length-1)] = 'k'
    if 'u' not in middle_chars:
        middle_chars[random.randint(0, middle_length-1)] = 'u'
    
    middle_part = ''.join(middle_chars)
    
    # 마지막 4글자는 gwan
    last_part = 'gwan'
    
    # 최종 이름 생성
    building_name = first_letter + middle_part + last_part
    
    # 정규표현식으로 조건 검증
    pattern = r'^n[a-z]*k[a-z]*u[a-z]*gwan$|^n[a-z]*u[a-z]*k[a-z]*gwan$'
    if not re.match(pattern, building_name):
        # k와 u가 포함되지 않았을 경우 다시 생성
        return generate_building_name()
    
    return building_name

# 조건을 만족하는 건물 이름 출력
print(generate_building_name())