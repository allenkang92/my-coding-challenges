-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131112?language=oracle
-- 간단한 문제 설명 : 
--   FOOD_FACTORY 테이블에서 강원도에 위치한 식품공장의 정보를 조회하는 문제입니다.
--
-- 테이블 스키마 :
--   - 테이블명 : FOOD_FACTORY
--   - 컬럼정보:
--       FACTORY_ID   VARCHAR(10)    NOT NULL  -- 공장 ID
--       FACTORY_NAME VARCHAR(50)    NOT NULL  -- 공장 이름
--       ADDRESS      VARCHAR(100)   NOT NULL  -- 주소
--       TLNO        VARCHAR(20)     NULL     -- 전화번호
--
-- 해결 방법 설명 :
--   1. SELECT 절에서 필요한 컬럼만 선택 (FACTORY_ID, FACTORY_NAME, ADDRESS)
--   2. WHERE 절에서 SUBSTR 함수를 사용하여 ADDRESS의 첫 3글자가 '강원도'인 데이터만 필터링
--   3. ORDER BY 절을 사용하여 FACTORY_ID 기준 오름차순 정렬
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N)
--       - N은 테이블의 전체 행 수입니다.
--       - ORDER BY로 인한 정렬 작업이 O(N log N)의 시간복잡도를 가집니다.
--   - 공간복잡도 : O(K)
--       - K는 '강원도'에 위치한 공장의 수입니다.
--       - 결과 집합을 저장하는데 필요한 공간입니다.

SELECT 
    FACTORY_ID,     -- 공장 ID 
    FACTORY_NAME,   -- 공장 이름
    ADDRESS         -- 주소
FROM 
    FOOD_FACTORY
WHERE 
    -- ADDRESS 컬럼에서 첫 번째 문자부터 3개의 문자를 추출(SUBSTR)하여 '강원도'와 비교
    -- SUBSTR(문자열, 시작위치, 길이)
    -- 시작위치: 1 (첫 번째 문자부터)
    -- 길이: 3 ('강원도'의 길이)
    SUBSTR(ADDRESS, 1, 3) = '강원도'
ORDER BY 
    FACTORY_ID ASC;  -- 공장 ID를 기준으로 오름차순 정렬