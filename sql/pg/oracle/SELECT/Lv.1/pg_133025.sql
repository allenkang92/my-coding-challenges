-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/133025?language=oracle
-- 간단한 문제 설명 : 
--   총주문량이 3,000 초과이면서 과일 기반인 아이스크림을 주문량 내림차순으로 조회
--
-- 테이블 스키마 :
--   - FIRST_HALF 테이블: 상반기 주문 정보
--     SHIPMENT_ID INT(N)    NOT NULL  -- 출하 번호
--     FLAVOR VARCHAR(N)     NOT NULL  -- 아이스크림 맛 (기본 키)
--     TOTAL_ORDER INT(N)    NOT NULL  -- 총주문량
--   
--   - ICECREAM_INFO 테이블: 아이스크림 성분 정보
--     FLAVOR VARCHAR(N)     NOT NULL  -- 아이스크림 맛 (기본 키, 외래 키)
--     INGREDIENT_TYPE VARCHAR(N) NOT NULL  -- 성분 타입
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N) - 정렬로 인해
--   - 공간복잡도 : O(N) - 결과 저장 공간

SELECT 
    FIRST_HALF.FLAVOR
FROM 
    FIRST_HALF
    JOIN ICECREAM_INFO 
        ON FIRST_HALF.FLAVOR = ICECREAM_INFO.FLAVOR
WHERE 
    FIRST_HALF.TOTAL_ORDER > 3000 
    AND ICECREAM_INFO.INGREDIENT_TYPE = 'fruit_based'
ORDER BY 
    FIRST_HALF.TOTAL_ORDER DESC;  -- ASC를 DESC로 변경