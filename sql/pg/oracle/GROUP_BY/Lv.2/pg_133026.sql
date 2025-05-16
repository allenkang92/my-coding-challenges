-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/133026?language=oracle
-- 간단한 문제 설명 : 
--   - FIRST_HALF 테이블과 ICECREAM_INFO 테이블을 활용하여 상반기 동안 각 아이스크림 성분 타입별 총 주문량을 계산
--   - 총 주문량이 작은 순서대로 결과를 정렬하며, 총 주문량을 나타내는 컬럼명은 TOTALORDER로 지정

-- -----------------------------------------------------------------------------------------
-- 테이블 스키마 :
--   - 테이블명 : FIRST_HALF
--     - SHIPMENT_ID		INT(N)	FALSE	-- 아이스크림 공장에서 아이스크림 가게까지의 출하 번호
--     - FLAVOR			VARCHAR(N)	FALSE	-- 아이스크림 맛
--     - TOTAL_ORDER		INT(N)	FALSE	-- 상반기 아이스크림 총주문량
--
--   - 테이블명 : ICECREAM_INFO
--     - FLAVOR				VARCHAR(N)	FALSE	-- 아이스크림 맛
--     - INGREDIENT_TYPE		VARCHAR(N)	FALSE	-- 아이스크림의 성분 타입 ('sugar_based' 또는 'fruit_based')
-- -----------------------------------------------------------------------------------------
-- 해결 방법 설명 :
--   1. FIRST_HALF 테이블과 ICECREAM_INFO 테이블을 FLAVOR 컬럼을 기준으로 내부 조인하여 아이스크림의 성분 타입과 주문량을 함께 조회
--   2. 조인된 결과에서 각 INGREDIENT_TYPE별로 TOTAL_ORDER를 합산하여 성분 타입별 총 주문량을 계산
--   3. 계산된 총 주문량을 기준으로 오름차순 정렬하여 결과를 출력

-- -----------------------------------------------------------------------------------------
-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT: 조회할 컬럼을 선택
--   - SUM(F.TOTAL_ORDER): 각 그룹별로 TOTAL_ORDER의 합을 계산
--   - FROM: 데이터를 조회할 테이블을 지정
--   - JOIN: 두 테이블을 특정 조건으로 결합
--   - ON: JOIN 조건을 명시
--   - GROUP BY: 특정 컬럼을 기준으로 데이터 그룹화
--   - ORDER BY: 결과를 특정 컬럼 기준으로 정렬
--   - ASC: 오름차순 정렬 지정
-- -----------------------------------------------------------------------------------------
-- 쿼리 최적화 방법 :
--   - FLAVOR 컬럼에 인덱스를 생성하여 조인 성능 향상
--     예시 인덱스 생성:
--       CREATE INDEX idx_first_half_flavor ON FIRST_HALF(FLAVOR);
--       CREATE INDEX idx_icecream_info_flavor ON ICECREAM_INFO(FLAVOR);
--   - 필요 없는 컬럼은 SELECT 절에 포함하지 않음으로써 데이터 스캔을 최소화
--   - SUM 함수 대신 COUNT 함수 사용 고려 (요구 사항에 따라 다름)
-- -----------------------------------------------------------------------------------------
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N)
--     -- 두 테이블을 조인하고 그룹화를 수행하므로 선형 시간 복잡도
--   - 공간복잡도 : O(K)
--     -- 그룹화된 결과를 저장하기 위한 공간 (K는 고유 INGREDIENT_TYPE의 수)
-- -----------------------------------------------------------------------------------------
-- 최종 쿼리
-- -------------------------------------------------------------------------------------------

SELECT 
    I.INGREDIENT_TYPE AS INGREDIENTTYPE, 
    SUM(F.TOTAL_ORDER) AS TOTALORDER  -- 각 성분 타입별 총 주문량을 계산
FROM 
    FIRST_HALF F
JOIN 
    ICECREAM_INFO I ON F.FLAVOR = I.FLAVOR  -- 두 테이블을 FLAVOR 컬럼으로 조인
GROUP BY 
    I.INGREDIENT_TYPE  -- 성분 타입별로 그룹화
ORDER BY 
    TOTALORDER ASC;  -- 총 주문량을 기준으로 오름차순 정렬