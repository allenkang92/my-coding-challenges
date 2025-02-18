# 문제 링크 (주석) : https://www.acmicpc.net/problem/20232
# 문제 설명:
#   Northwestern Russia Regional Contest의 문제 출제 팀이 개최한 지역 대회 역사를 기반으로,
#   년도를 입력받아 해당 연도의 대회 우승 팀을 출력하는 프로그램을 작성하라.
#
#   아래는 대회 우승 결과 목록이다:
#       1995: ITMO
#       1996: SPbSU
#       1997: SPbSU
#       1998: ITMO
#       1999: ITMO
#       2000: SPbSU
#       2001: ITMO
#       2002: ITMO
#       2003: ITMO
#       2004: ITMO
#       2005: ITMO
#       2006: PetrSU, ITMO
#       2007: SPbSU
#       2008: SPbSU
#       2009: ITMO
#       2010: ITMO
#       2011: ITMO
#       2012: ITMO
#       2013: SPbSU
#       2014: ITMO
#       2015: ITMO
#       2016: ITMO
#       2017: ITMO
#       2018: SPbSU
#       2019: ITMO
#
# 해결 방법:
#   year를 입력받아 위 목록에 따라 대응하는 우승 팀 이름을 출력한다.
#
# 시간/공간 복잡도 : O(1)

y = int(input())

contest_dict = {
    "1995": "ITMO",
    "1996": "SPbSU",
    "1997": "SPbSU",
    "1998": "ITMO",
    "1999": "ITMO",
    "2000": "SPbSU",
    "2001": "ITMO",
    "2002": "ITMO",
    "2003": "ITMO",
    "2004": "ITMO",
    "2005": "ITMO",
    "2006": "PetrSU, ITMO",
    "2007": "SPbSU",
    "2008": "SPbSU",
    "2009": "ITMO",
    "2010": "ITMO",
    "2011": "ITMO",
    "2012": "ITMO",
    "2013": "SPbSU",
    "2014": "ITMO",
    "2015": "ITMO",
    "2016": "ITMO",
    "2017": "ITMO",
    "2018": "SPbSU",
    "2019": "ITMO"
}

print(contest_dict[str(y)])