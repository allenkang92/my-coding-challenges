-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/131116
-- 간단한 문제 설명 : 
--   - FOOD_PRODUCT 테이블을 이용하여 식품분류별로 가장 비싼 식품의 정보를 조회.
--   - 식품분류가 '과자', '국', '김치', '식용유'인 경우만 포함.
--   - 결과는 CATEGORY, MAX_PRICE, PRODUCT_NAME을 출력.
--   - 결과는 식품 가격을 기준으로 내림차순 정렬.

-- 테이블 스키마 :
--   - 테이블명 : FOOD_PRODUCT
--     - PRODUCT_ID VARCHAR(10) FALSE -- 식품 ID
--     - PRODUCT_NAME VARCHAR(50) FALSE -- 식품 이름
--     - PRODUCT_CD VARCHAR(10) TRUE -- 식품 코드
--     - CATEGORY VARCHAR(10) TRUE -- 식품 분류
--     - PRICE NUMBER TRUE -- 식품 가격

-- 해결 방법 설명 :
--   1. 특정 카테고리('과자', '국', '김치', '식용유')에 해당하는 상품만 필터링.
--   2. 서브쿼리를 사용하여 각 카테고리별 최대 가격을 구함.
--   3. 서브쿼리의 결과와 원본 테이블을 INNER JOIN하여 최대 가격에 해당하는 상품을 선택.
--   4. 필요한 컬럼(CATEGORY, MAX_PRICE, PRODUCT_NAME)을 선택.
--   5. PRICE를 기준으로 내림차순 정렬.

-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT: 특정 컬럼을 선택하여 조회.
--   - AS: 컬럼에 별칭을 부여하여 결과를 보기 쉽게 만듦.
--   - FROM: 데이터를 조회할 테이블을 지정.
--   - INNER JOIN: 두 테이블을 특정 조건에 맞춰 결합.
--   - ON: JOIN할 때 사용할 조건을 명시.
--   - WHERE: 조건에 맞는 데이터를 필터링.
--   - IN: 특정 값 집합 내에서 일치하는 값을 찾기 위해 사용.
--   - MAX(): 집계 함수로 최대 값을 구함.
--   - GROUP BY: 특정 컬럼을 기준으로 그룹화.
--   - ORDER BY: 결과를 정렬.

-- 쿼리 최적화 방법 (인덱스 사용, 조인 방식 등) :
--   - 인덱스 생성:
--       * FOOD_PRODUCT 테이블의 CATEGORY, PRICE 컬럼에 인덱스를 생성하여 검색 속도를 향상시킴.
--       ```sql
--       CREATE INDEX idx_food_product_category_price ON FOOD_PRODUCT (CATEGORY, PRICE);
--       ```
--   - 조인 방식 최적화:
--       * INNER JOIN을 사용하여 서브쿼리의 최대 가격과 메인 쿼리를 결합함으로써 불필요한 데이터 로드를 줄임.
--       * 필요한 컬럼만 선택하여 데이터 처리량을 최소화함.
--   - WHERE 절 최적화:
--       * IN 연산자를 사용하여 특정 카테고리를 필터링함으로써 인덱스를 효과적으로 활용함.

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N), N은 FOOD_PRODUCT 테이블의 레코드 수. 서브쿼리와 JOIN 연산이 포함됨.
--   - 공간복잡도 : O(K), K는 결과로 반환되는 레코드의 수. 인덱스는 데이터베이스 엔진에 의해 관리됨.

SELECT 
    fp.CATEGORY, 
    fp.PRICE AS MAX_PRICE, 
    fp.PRODUCT_NAME
FROM 
    FOOD_PRODUCT fp
INNER JOIN (
    SELECT 
        CATEGORY, 
        MAX(PRICE) AS MAX_PRICE
    FROM 
        FOOD_PRODUCT
    WHERE 
        CATEGORY IN ('과자', '국', '김치', '식용유')
    GROUP BY 
        CATEGORY
) sub
ON 
    fp.CATEGORY = sub.CATEGORY AND
    fp.PRICE = sub.MAX_PRICE
WHERE 
    fp.CATEGORY IN ('과자', '국', '김치', '식용유')
ORDER BY 
    fp.PRICE DESC;