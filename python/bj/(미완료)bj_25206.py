# 문제 링크 : https://www.acmicpc.net/problem/25206
# 간단한 문제 설명 : 
# 해결 방법 설명 : 
# 시간/공간 복잡도 : 

subject = []
score = []
grade = []
agg = 0
for i in range(20):
    subject, score, grade = input().split(" ")

for j in grade:
    if j == "P":
        score.remove["P"]
    elif j == "F":
        agg += 0.0
    elif j == "D0":
        agg += 1.0
    elif j == "D+":
        agg += 1.5
    elif j == "C0":
        agg += 2.0
    elif j == "C+":
        agg += 2.5
    elif j == "B0":
        agg += 3.0
    elif j == "B+":
        agg += 3.5
    elif j == "A0":
        agg += 4.0
    elif j == "A+":
        agg += 4.5

print(agg/(len(score)-1))