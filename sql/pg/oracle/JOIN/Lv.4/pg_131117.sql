-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131117
-- 간단한 문제 설명 : 
--   - FOOD_PRODUCT와 FOOD_ORDER 테이블을 이용하여 2022년 5월 생산된 식품들의 총매출을 조회.
--   - 결과는 PRODUCT_ID, PRODUCT_NAME, TOTAL_SALES를 출력.
--   - 총매출 기준 내림차순 정렬, 동일 매출 시 PRODUCT_ID 기준 오름차순 정렬.

-- 테이블 스키마 :
--   - 테이블명 : FOOD_PRODUCT
--     - PRODUCT_ID VARCHAR(10) FALSE -- 식품 ID
--     - PRODUCT_NAME VARCHAR(50) FALSE -- 식품 이름
--     - PRODUCT_CD VARCHAR(10) TRUE -- 식품 코드
--     - CATEGORY VARCHAR(10) TRUE -- 식품 분류
--     - PRICE NUMBER TRUE -- 식품 가격
--   
--   - 테이블명 : FOOD_ORDER
--     - ORDER_ID VARCHAR(10) FALSE -- 주문 ID
--     - PRODUCT_ID VARCHAR(5) FALSE -- 제품 ID
--     - AMOUNT NUMBER FALSE -- 주문량
--     - PRODUCE_DATE DATE TRUE -- 생산일자
--     - IN_DATE DATE TRUE -- 입고일자
--     - OUT_DATE DATE TRUE -- 출고일자
--     - FACTORY_ID VARCHAR(10) FALSE -- 공장 ID
--     - WAREHOUSE_ID VARCHAR(10) FALSE -- 창고 ID

-- 해결 방법 설명 :
--   1. FOOD_PRODUCT와 FOOD_ORDER를 PRODUCT_ID 기준으로 INNER JOIN.
--   2. PRODUCE_DATE가 2022년 5월인 주문만 필터링.
--      - TO_CHAR 함수 사용 대신 날짜 범위를 직접 지정하여 인덱스 활용 최적화.
--   3. 각 제품별 총매출(TOTAL_SALES)을 SUM 함수를 사용하여 계산.
--   4. GROUP BY는 PRODUCT_ID와 PRODUCT_NAME으로 설정하여 집계.
--   5. TOTAL_SALES를 기준으로 내림차순, 동일 시 PRODUCT_ID를 기준으로 오름차순 정렬.

-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT: 특정 컬럼을 선택하여 조회.
--   - SUM(): 지정한 표현식의 합계를 계산하는 집계 함수.
--   - AS: 컬럼에 별칭을 부여하여 결과를 보기 쉽게 함.
--   - FROM: 데이터를 조회할 테이블을 지정.
--   - INNER JOIN: 두 테이블을 특정 조건에 맞춰 결합.
--   - ON: JOIN할 때 사용할 조건을 명시.
--   - WHERE: 특정 조건에 맞는 데이터를 필터링.
--   - DATE: 날짜 리터럴을 지정.
--   - GROUP BY: 특정 컬럼을 기준으로 데이터를 그룹화.
--   - ORDER BY: 결과를 특정 컬럼을 기준으로 정렬.

-- 쿼리 최적화 방법 (인덱스 사용, 조인 방식 등) :
--   - 인덱스 생성:
--       * FOOD_PRODUCT 테이블의 PRODUCT_ID에 인덱스를 생성하여 JOIN 성능 향상.
--       * FOOD_ORDER 테이블의 PRODUCT_ID와 PRODUCE_DATE에 복합 인덱스를 생성하여 WHERE 절 필터링 및 JOIN 성능 향상.
--       ```sql
--       CREATE INDEX idx_food_product_product_id ON FOOD_PRODUCT (PRODUCT_ID);
--       CREATE INDEX idx_food_order_product_id_produce_date ON FOOD_ORDER (PRODUCT_ID, PRODUCE_DATE);
--       ```
--   - 조인 방식 최적화:
--       * INNER JOIN을 사용하여 두 테이블 간의 매칭되는 레코드만 결합함으로써 불필요한 데이터 로드 감소.
--       * 필요한 컬럼만 SELECT 절에 포함시켜 데이터 처리량 최소화.
--   - WHERE 절 최적화:
--       * TO_CHAR 함수 사용 대신 날짜 범위를 직접 지정하여 인덱스 활용을 극대화.
--       * 예: PRODUCE_DATE >= DATE '2022-05-01' AND PRODUCE_DATE < DATE '2022-06-01'

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N), N은 FOOD_ORDER 테이블의 레코드 수. JOIN과 GROUP BY 연산이 포함됨.
--   - 공간복잡도 : O(K), K는 결과로 반환되는 레코드 수. 인덱스는 데이터베이스 엔진에 의해 관리됨.

SELECT 
    A.PRODUCT_ID, 
    A.PRODUCT_NAME, 
    SUM(A.PRICE * B.AMOUNT) AS TOTAL_SALES
FROM 
    FOOD_PRODUCT A
INNER JOIN 
    FOOD_ORDER B 
    ON A.PRODUCT_ID = B.PRODUCT_ID
WHERE 
    B.PRODUCE_DATE >= DATE '2022-05-01' 
    AND B.PRODUCE_DATE < DATE '2022-06-01'
GROUP BY 
    A.PRODUCT_ID, 
    A.PRODUCT_NAME
ORDER BY 
    TOTAL_SALES DESC, 
    A.PRODUCT_ID ASC;