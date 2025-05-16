-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131536?language=oracle
-- 간단한 문제 설명 :
--   - ONLINE_SALE 테이블에서 동일한 회원이 동일한 상품을 재구매한 데이터를 구함
--   - 재구매한 회원 ID와 재구매한 상품 ID를 출력
--   - 결과는 회원 ID를 기준으로 오름차순 정렬하고, 회원 ID가 같다면 상품 ID를 기준으로 내림차순 정렬

-- -----------------------------------------------------------------------------------------
-- 테이블 스키마 (ONLINE_SALE):
--   - ONLINE_SALE_ID INTEGER    NOT NULL  -- 온라인 상품 판매 ID
--   - USER_ID        INTEGER    NOT NULL  -- 회원 ID
--   - PRODUCT_ID     INTEGER    NOT NULL  -- 상품 ID
--   - SALES_AMOUNT   INTEGER    NOT NULL  -- 판매량
--   - SALES_DATE     DATE       NOT NULL  -- 판매일
-- -----------------------------------------------------------------------------------------
-- 해결 방법 설명:
--   1. GROUP BY 절을 사용하여 USER_ID와 PRODUCT_ID별로 데이터를 그룹화
--   2. HAVING 절에서 COUNT(*) > 1 조건을 사용하여 재구매(같은 USER_ID와 PRODUCT_ID의 구매 횟수가 2회 이상인 경우) 필터링
--   3. SELECT 절에서 USER_ID와 PRODUCT_ID를 선택
--   4. ORDER BY 절을 사용하여 USER_ID는 오름차순, PRODUCT_ID는 내림차순으로 정렬
--
-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT: 원하는 컬럼을 선택
--   - FROM: 데이터 소스 테이블 지정
--   - GROUP BY: 특정 컬럼을 기준으로 데이터 그룹화
--   - HAVING: 그룹화된 데이터에 조건 적용
--   - COUNT(*) > 1: 그룹 내 행의 개수가 2 이상인 경우(재구매)만 선택
--   - ORDER BY: 결과 정렬 기준 지정 (USER_ID ASC, PRODUCT_ID DESC)
--
-- 쿼리 최적화 방법 :
--   - USER_ID와 PRODUCT_ID 컬럼에 복합 인덱스를 생성하면 GROUP BY 및 HAVING 절의 성능을 향상시킬 수 있음
--   - 인덱스는 데이터베이스의 조회 속도를 크게 향상시킬 수 있는 중요한 요소이지만, 너무 많은 인덱스는 쓰기 성능을 저하시킬 수 있으므로 주의가 필요함
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N) - GROUP BY와 정렬로 인해
--   - 공간복잡도 : O(K) - 그룹화된 결과 저장 공간 (K는 그룹의 수)

-- -------------------------------------------------------------------------------------------
-- 최종 쿼리
-- -------------------------------------------------------------------------------------------

SELECT 
    USER_ID,                                           -- 재구매한 회원 ID
    PRODUCT_ID                                         -- 재구매한 상품 ID
FROM 
    ONLINE_SALE                                        -- 데이터 소스 테이블
GROUP BY 
    USER_ID, PRODUCT_ID                                -- 회원 ID와 상품 ID별로 그룹화
HAVING 
    COUNT(*) > 1                                       -- 동일한 그룹의 행 개수가 2개 이상인 경우 (재구매)
ORDER BY 
    USER_ID ASC,                                       -- 회원 ID를 기준으로 오름차순 정렬
    PRODUCT_ID DESC;                                   -- 회원 ID가 같을 경우 상품 ID를 기준으로 내림차순 정렬

-- -------------------------------------------------------------------------------------------
-- 추가 최적화: COUNT(DISTINCT SALES_DATE) > 1 사용 예시
-- -------------------------------------------------------------------------------------------

-- 동일한 상품을 다른 날짜에 구매한 경우만 재구매로 간주하고 싶다면, COUNT(DISTINCT SALES_DATE) > 1을 사용할 수 있습니다.

SELECT 
    USER_ID, 
    PRODUCT_ID
FROM 
    ONLINE_SALE
GROUP BY 
    USER_ID, PRODUCT_ID
HAVING 
    COUNT(DISTINCT SALES_DATE) > 1
ORDER BY 
    USER_ID ASC, 
    PRODUCT_ID DESC;

-- -------------------------------------------------------------------------------------------
-- 추가 최적화: 자가 조인(Self-Join) 사용 예시
-- -------------------------------------------------------------------------------------------

-- 재구매를 찾기 위해 SELF JOIN을 사용하는 방법도 있습니다. 이 방법은 동일한 USER_ID와 PRODUCT_ID를 가진 두 개 이상의 레코드를 찾는 데 유용합니다.

SELECT DISTINCT 
    a.USER_ID, 
    a.PRODUCT_ID
FROM 
    ONLINE_SALE a
JOIN 
    ONLINE_SALE b
  ON a.USER_ID = b.USER_ID 
 AND a.PRODUCT_ID = b.PRODUCT_ID
 AND a.ONLINE_SALE_ID < b.ONLINE_SALE_ID
ORDER BY 
    a.USER_ID ASC, 
    a.PRODUCT_ID DESC;

-- -------------------------------------------------------------------------------------------
-- 추가 설명:
--
-- 1. **GROUP BY와 HAVING 절**:
--    - `GROUP BY USER_ID, PRODUCT_ID`로 각 회원과 상품 조합을 그룹화합니다.
--    - `HAVING COUNT(*) > 1`은 해당 조합이 2번 이상 발생한 경우만 선택합니다.
--
-- 2. **ORDER BY 절**:
--    - `ORDER BY USER_ID ASC, PRODUCT_ID DESC`로 결과를 정렬합니다.
--    - 먼저 `USER_ID`를 기준으로 오름차순 정렬하고, 동일한 `USER_ID` 내에서는 `PRODUCT_ID`를 기준으로 내림차순 정렬합니다.
--
-- 3. **인덱스 생성**:
--    - `CREATE INDEX idx_user_product ON ONLINE_SALE(USER_ID, PRODUCT_ID);` 
--    - 이 인덱스는 `GROUP BY`와 `HAVING` 절의 성능을 향상시킵니다.
--    - 인덱스는 데이터를 빠르게 조회할 수 있게 도와주지만, 너무 많은 인덱스는 쓰기 작업에 영향을 줄 수 있습니다.
--
-- 4. **성능 최적화**:
--    - 복합 인덱스를 사용하면 `GROUP BY`와 같은 집계 연산의 성능을 향상시킬 수 있습니다.
--    - 데이터베이스가 인덱스를 효율적으로 활용할 수 있도록 쿼리를 작성하는 것이 중요합니다.
--
-- 5. **대체 방법**:
--    - `COUNT(DISTINCT SALES_DATE) > 1`을 사용하여 동일한 상품을 다른 날짜에 여러 번 구매한 경우로 재구매를 정의할 수 있습니다.
--    - `SELF JOIN`을 사용하여 재구매를 찾는 방법도 가능합니다. 이 방법은 동일한 `USER_ID`와 `PRODUCT_ID`를 가지는 두 개 이상의 레코드를 찾는 데 유용합니다.
--
-- 6. **시간/공간 복잡도**:
--    - `GROUP BY`와 `HAVING` 절을 사용하는 경우, 시간복잡도는 데이터 양에 따라 다르지만 일반적으로 O(N log N)입니다.
--    - 공간복잡도는 그룹화된 결과의 수에 비례하며, 이는 O(K)입니다. (K는 그룹의 수)
--
-- -------------------------------------------------------------------------------------------