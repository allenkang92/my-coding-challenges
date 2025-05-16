-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131533?language=oracle
-- 간단한 문제 설명 : 
--   - PRODUCT 테이블과 OFFLINE_SALE 테이블을 조인하여 상품코드 별 매출액 합계를 조회
--   - 매출액은 판매가(PRICE) * 판매량(SALES_AMOUNT)으로 계산
--   - 결과는 매출액을 기준으로 내림차순 정렬, 매출액이 같다면 상품코드를 기준으로 오름차순 정렬
--   - 결과 컬럼명은 PRODUCT_CODE, SALES로 지정

-- -----------------------------------------------------------------------------------------
-- 테이블 스키마 :
--   - PRODUCT 테이블:
--     - PRODUCT_ID     INTEGER       NOT NULL  -- 상품 ID
--     - PRODUCT_CODE   VARCHAR(8)    NOT NULL  -- 상품 코드
--     - PRICE          INTEGER       NOT NULL  -- 판매가
--
--   - OFFLINE_SALE 테이블:
--     - OFFLINE_SALE_ID INTEGER      NOT NULL  -- 오프라인 판매 ID
--     - PRODUCT_ID      INTEGER      NOT NULL  -- 상품 ID
--     - SALES_AMOUNT    INTEGER      NOT NULL  -- 판매량
--     - SALES_DATE      DATE         NOT NULL  -- 판매일
-- -----------------------------------------------------------------------------------------
-- 해결 방법 설명:
--   1. PRODUCT 테이블과 OFFLINE_SALE 테이블을 PRODUCT_ID로 INNER JOIN
--   2. 상품코드별로 그룹화(GROUP BY PRODUCT_CODE)
--   3. 매출액(SALES)을 SUM(PRICE * SALES_AMOUNT)으로 계산
--   4. 매출액을 기준으로 내림차순, 상품코드를 기준으로 오름차순 정렬
--
-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT: 원하는 컬럼 선택
--   - INNER JOIN: 두 테이블을 조건에 맞게 결합
--   - GROUP BY: 특정 컬럼을 기준으로 그룹화
--   - SUM: 합계 계산 함수
--   - ORDER BY: 결과 정렬
--
-- 쿼리 최적화 방법 :
--   - PRODUCT 테이블의 PRODUCT_ID와 OFFLINE_SALE 테이블의 PRODUCT_ID에 인덱스를 생성하여 조인 성능 향상
--   - 인덱스 예시:
--     CREATE INDEX idx_product_id ON PRODUCT(PRODUCT_ID);
--     CREATE INDEX idx_offline_sale_product_id ON OFFLINE_SALE(PRODUCT_ID);
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N) - 테이블 조인 및 그룹화 연산
--   - 공간복잡도 : O(K) - 그룹화된 결과 저장 공간 (K는 고유 상품코드의 수)

-- -------------------------------------------------------------------------------------------
-- 최종 쿼리
-- -------------------------------------------------------------------------------------------

SELECT 
    A.PRODUCT_CODE,                                 -- 상품 코드
    SUM(A.PRICE * B.SALES_AMOUNT) AS SALES         -- 매출액 합계
FROM 
    PRODUCT A
INNER JOIN 
    OFFLINE_SALE B ON A.PRODUCT_ID = B.PRODUCT_ID  -- PRODUCT_ID로 조인
GROUP BY 
    A.PRODUCT_CODE                                   -- 상품 코드별 그룹화
ORDER BY 
    SALES DESC,                                      -- 매출액 내림차순
    A.PRODUCT_CODE ASC;                              -- 상품코드 오름차순

-- -------------------------------------------------------------------------------------------
-- 추가 최적화: 서브쿼리를 사용한 매출액 계산 방법
-- -------------------------------------------------------------------------------------------

-- 서브쿼리를 사용하여 매출액을 미리 계산한 후 정렬하는 방법입니다.
-- 이 방법도 동일한 결과를 반환하며, 인덱스가 잘 활용될 경우 성능 향상을 기대할 수 있습니다.

-- SELECT 
--     PRODUCT_CODE,
--     SALES
-- FROM (
--     SELECT 
--         A.PRODUCT_CODE,
--         SUM(A.PRICE * B.SALES_AMOUNT) AS SALES
--     FROM 
--         PRODUCT A
--     INNER JOIN 
--         OFFLINE_SALE B ON A.PRODUCT_ID = B.PRODUCT_ID
--     GROUP BY 
--         A.PRODUCT_CODE
-- ) 
-- ORDER BY 
--     SALES DESC,
--     PRODUCT_CODE ASC;

-- -------------------------------------------------------------------------------------------
-- 쿼리 실행 예시
-- -------------------------------------------------------------------------------------------

-- 제공된 예시 데이터를 기준으로 쿼리를 실행하면 다음과 같은 결과가 출력됩니다:
--
-- | PRODUCT_CODE | SALES  |
-- |--------------|--------|
-- | C3000002     | 126000 |
-- | A1000011     | 90000  |
-- | A1000045     | 16000  |
--
-- -------------------------------------------------------------------------------------------
-- 추가 설명:
--
-- 1. **INNER JOIN**:
--    - PRODUCT 테이블과 OFFLINE_SALE 테이블을 PRODUCT_ID로 조인하여 관련 데이터를 결합합니다.
--
-- 2. **SUM(PRICE * SALES_AMOUNT) AS SALES**:
--    - 각 상품의 매출액을 판매가와 판매량을 곱하여 합산합니다.
--
-- 3. **GROUP BY A.PRODUCT_CODE**:
--    - 상품코드별로 데이터를 그룹화하여 매출액을 계산합니다.
--
-- 4. **ORDER BY SALES DESC, A.PRODUCT_CODE ASC**:
--    - 매출액을 기준으로 내림차순 정렬하고, 매출액이 동일한 경우 상품코드를 기준으로 오름차순 정렬합니다.
--
-- 5. **쿼리 오류 수정**:
--    - 원래 HAVING 절에 잘못된 조건이 포함되어 있었으나, 매출액 필터링이 필요한 경우 HAVING 절을 올바르게 사용해야 합니다.
--    - 현재 문제에서는 모든 매출 데이터를 포함하므로 HAVING 절이 불필요합니다.
--
-- 6. **오류 원인 분석**:
--    - 원래 쿼리에서 HAVING 절에 `SUM(A.SALES)`와 같은 잘못된 표현이 사용되었습니다.
--    - 또한, SELECT 절에서 `A.SALES`는 존재하지 않는 컬럼으로, 올바른 매출액 계산이 필요했습니다.
--    - ORDER BY 절에서 `A.PRICE`는 GROUP BY 절에 포함되지 않았으므로 오류가 발생했습니다.
--    - 이를 수정하여 매출액을 올바르게 계산하고 정렬 기준을 조정했습니다.
--
-- -------------------------------------------------------------------------------------------