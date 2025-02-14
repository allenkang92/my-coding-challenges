# 문제 링크 (주석) : https://www.acmicpc.net/problem/30676
# 간단한 문제 설명 : 주어진 파장에 따라 별의 색을 출력하는 문제
# 해결 방법 설명 : 파장 범위에 따라 해당하는 색을 출력
# 시간/공간 복잡도 : O(1)

lam = int(input())

if 620 <= lam <= 780:
    print("Red")

elif 590 <= lam < 620:
    print("Orange")

elif 570 <= lam < 590:
    print("Yellow")
 
elif 495 <= lam < 570:
    print("Green")

elif 450 <= lam < 495:
   print("Blue")

elif 425 <= lam < 450:
   print("Indigo")

elif 380 <= lam < 425:
    print("Violet")