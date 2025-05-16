-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131115?language=oracle
-- 간단한 문제 설명 : 
--   - FOOD_PRODUCT 테이블에서 가격이 가장 비싼 식품의 정보를 조회
--   - 결과 컬럼명은 문제에 맞게 지정 (예: PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE)

-- -----------------------------------------------------------------------------------------
-- 테이블 스키마 (FOOD_PRODUCT):
--   - PRODUCT_ID     VARCHAR(10)    NOT NULL  -- 식품 ID
--   - PRODUCT_NAME   VARCHAR(50)    NOT NULL  -- 식품 이름
--   - PRODUCT_CD     VARCHAR(10)         -- 식품 코드 (NULL 가능)
--   - CATEGORY       VARCHAR(10)         -- 식품분류 (NULL 가능)
--   - PRICE          NUMBER              -- 식품 가격 (NULL 가능)
-- -----------------------------------------------------------------------------------------
-- 해결 방법 설명:
--   1. SELECT 절에서 필요한 컬럼(PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE)을 선택
--   2. ORDER BY 절을 사용하여 PRICE를 기준으로 내림차순 정렬
--   3. FETCH FIRST ROW ONLY를 사용하여 가장 높은 가격의 식품 한 개만 조회
--
-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT: 원하는 컬럼을 선택
--   - FROM: 데이터를 조회할 테이블 지정
--   - ORDER BY: 특정 컬럼을 기준으로 데이터 정렬
--   - DESC: 내림차순 정렬
--   - FETCH FIRST ROW ONLY: 정렬된 결과에서 첫 번째 행만 조회
--
-- 쿼리 최적화 방법 :
--   - PRICE 컬럼에 인덱스를 생성하면 ORDER BY 절의 정렬 성능을 향상시킬 수 있음
--   - 인덱스는 데이터베이스의 조회 속도를 크게 향상시킬 수 있는 중요한 요소이지만, 너무 많은 인덱스는 쓰기 성능을 저하시킬 수 있으므로 주의가 필요함
--
--   예시 인덱스 생성:
--     CREATE INDEX idx_food_product_price ON FOOD_PRODUCT(PRICE);
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N) - PRICE 기준 정렬에 따른 시간
--   - 공간복잡도 : O(1) - 단일 행 조회로 인한 공간 사용 최소화
--
-- -------------------------------------------------------------------------------------------
-- 최종 쿼리
-- -------------------------------------------------------------------------------------------

SELECT 
    PRODUCT_ID,            -- 식품 ID
    PRODUCT_NAME,          -- 식품 이름
    PRODUCT_CD,            -- 식품 코드
    CATEGORY,              -- 식품분류
    PRICE                  -- 식품 가격
FROM 
    FOOD_PRODUCT           -- 데이터 소스 테이블
ORDER BY 
    PRICE DESC             -- PRICE를 기준으로 내림차순 정렬
FETCH FIRST ROW ONLY;     -- 가장 높은 가격의 식품 한 개만 조회

-- -------------------------------------------------------------------------------------------
-- 추가 최적화: 서브쿼리를 사용한 최대 가격 조회 방법
-- -------------------------------------------------------------------------------------------

-- 서브쿼리를 사용하여 최대 가격을 먼저 조회한 후, 해당 가격을 가진 식품의 정보를 가져오는 방법입니다.
-- 이 방법은 PRICE 컬럼에 인덱스가 있을 경우 성능 향상을 기대할 수 있습니다.

SELECT 
    PRODUCT_ID,            -- 식품 ID
    PRODUCT_NAME,          -- 식품 이름
    PRODUCT_CD,            -- 식품 코드
    CATEGORY,              -- 식품분류
    PRICE                  -- 식품 가격
FROM 
    FOOD_PRODUCT
WHERE 
    PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT)  -- PRICE가 최대인 행만 선택
FETCH FIRST ROW ONLY;                             -- 동일한 가격을 가진 다중 행 중 첫 번째 행만 조회

-- -------------------------------------------------------------------------------------------
-- 추가 설명:
--
-- 1. **ORDER BY 절과 FETCH FIRST ROW ONLY**:
--    - ORDER BY PRICE DESC는 PRICE를 기준으로 내림차순 정렬하여 가장 비싼 식품이 먼저오도록 합니다.
--    - FETCH FIRST ROW ONLY는 정렬된 결과 중 첫 번째 행만 조회하므로, 가장 비싼 식품의 정보만 반환됩니다.
--
-- 2. **서브쿼리 방식**:
--    - 서브쿼리 `(SELECT MAX(PRICE) FROM FOOD_PRODUCT)`는 FOOD_PRODUCT 테이블에서 PRICE의 최대값을 구합니다.
--    - WHERE 절에서 PRICE가 이 최대값과 일치하는 행을 선택하여 가장 비싼 식품의 정보를 조회합니다.
--
-- 3. **인덱스 활용**:
--    - PRICE 컬럼에 인덱스를 생성하면 ORDER BY와 MAX 함수의 성능을 향상시킬 수 있습니다.
--    - 예를 들어, `CREATE INDEX idx_food_product_price ON FOOD_PRODUCT(PRICE);`를 통해 인덱스를 생성할 수 있습니다.
--
-- 4. **다중 최고 가격 대응**:
--    - 만약 여러 행이 동일한 최대 PRICE를 가질 경우, FETCH FIRST ROW ONLY를 사용하면 그 중 첫 번째 행만 반환됩니다.
--    - 모든 최고 가격의 행을 조회하고자 할 경우, FETCH FIRST ROW ONLY를 제거하거나 다른 조건을 추가할 수 있습니다.
--
-- 5. **성능 고려사항**:
--    - ORDER BY와 FETCH FIRST ROW ONLY를 사용하는 방법은 간단하지만, 대규모 테이블에서는 정렬 작업이 비용이 많이 들 수 있습니다.
--    - 서브쿼리 방식은 최대값을 먼저 조회한 후 해당 값을 가진 행을 선택하므로, 인덱스가 잘 설계된 경우 더 효율적일 수 있습니다.
--
-- 6. **실제 데이터 적용**:
--    - 예시 데이터에서는 PRICE가 6500인 P0020이 가장 비싼 식품입니다.
--    - 따라서, 위의 쿼리를 실행하면 다음과 같은 결과가 출력됩니다:
--
--    | PRODUCT_ID | PRODUCT_NAME | PRODUCT_CD  | CATEGORY | PRICE |
--    |------------|--------------|-------------|----------|-------|
--    | P0020      | 맛있는산초유 | CD_OL00010  | 식용유   | 6500  |
--
-- -------------------------------------------------------------------------------------------