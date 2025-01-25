-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/133027
-- 간단한 문제 설명 : 
--   - 상반기와 7월 아이스크림 주문량 합계가 많은 상위 3개 맛 조회
--   - 같은 맛이라도 다른 출하번호를 가질 수 있음

-- 테이블 스키마 :
--   - 테이블명 : FIRST_HALF
--     - SHIPMENT_ID INT(N) FALSE -- 출하 번호
--     - FLAVOR VARCHAR(N) FALSE -- 아이스크림 맛
--     - TOTAL_ORDER INT(N) FALSE -- 상반기 총주문량
--
--   - 테이블명 : JULY
--     - SHIPMENT_ID INT(N) FALSE -- 출하 번호
--     - FLAVOR VARCHAR(N) FALSE -- 아이스크림 맛
--     - TOTAL_ORDER INT(N) FALSE -- 7월 총주문량

-- 해결 방법 설명 :
--   1. 서브쿼리에서 JULY 테이블의 맛별 총 주문량 계산
--   2. FIRST_HALF와 FLAVOR 기준으로 JOIN
--   3. 두 테이블의 주문량 합계로 정렬 후 상위 3개 추출

-- 사용한 SQL 문법 및 함수 설명 :
--   - JOIN: 테이블 결합
--   - GROUP BY: 맛별 집계
--   - SUM: 주문량 합계 계산
--   - ORDER BY: 정렬
--   - FETCH FIRST n ROWS: 상위 n개 행 선택

-- 쿼리 최적화 방법 :
--   - 서브쿼리로 JULY 데이터 미리 집계하여 조인 부하 감소
--   - FLAVOR 인덱스 활용 조인
--   - 필요한 컬럼만 선택하여 데이터 처리량 최소화

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N), N은 전체 주문 수
--   - 공간복잡도 : O(M), M은 고유한 맛의 수

SELECT 
    A.FLAVOR
FROM 
    FIRST_HALF A
JOIN (
    SELECT 
        FLAVOR, 
        SUM(TOTAL_ORDER) AS JULY_TOTAL
    FROM 
        JULY
    GROUP BY 
        FLAVOR
) B ON A.FLAVOR = B.FLAVOR
ORDER BY 
    (A.TOTAL_ORDER + B.JULY_TOTAL) DESC
FETCH FIRST 3 ROWS ONLY;