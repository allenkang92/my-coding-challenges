-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131529?language=oracle
-- 간단한 문제 설명 : 
--   - PRODUCT 테이블에서 상품 카테고리 코드(PRODUCT_CODE 앞 2자리) 별 상품 개수를 조회
--   - 결과는 카테고리 코드를 기준으로 오름차순 정렬

-- -----------------------------------------------------------------------------------------
-- 테이블 스키마 :
--   - PRODUCT 테이블:
--     - PRODUCT_ID   INTEGER    NOT NULL  -- 상품 ID
--     - PRODUCT_CODE VARCHAR(8) NOT NULL  -- 상품 코드 (앞 2자리는 카테고리 코드)
--     - PRICE        INTEGER    NOT NULL  -- 판매가 (원)
-- -----------------------------------------------------------------------------------------
-- 해결 방법 설명:
--   1. PRODUCT 테이블에서 PRODUCT_CODE의 앞 2자리를 추출하여 카테고리 코드로 사용
--   2. 추출한 카테고리 코드별로 상품의 개수를 COUNT(*) 함수를 사용하여 계산
--   3. GROUP BY 절을 사용하여 카테고리 코드별로 그룹화
--   4. ORDER BY 절을 사용하여 카테고리 코드를 기준으로 오름차순 정렬

-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT: 조회할 컬럼을 선택
--   - SUBSTR(string, start_position, length): 문자열의 일부분을 추출
--   - COUNT(*): 그룹별 행의 개수를 계산
--   - FROM: 데이터를 조회할 테이블 지정
--   - GROUP BY: 특정 컬럼을 기준으로 그룹화
--   - ORDER BY: 결과를 특정 컬럼 기준으로 정렬

-- 쿼리 최적화 방법 :
--   - PRODUCT_CODE 컬럼에 인덱스를 생성하여 SUBSTR 함수 사용 시 인덱스 활용 가능
--     예시 인덱스 생성:
--       CREATE INDEX idx_product_code ON PRODUCT(PRODUCT_CODE);
--   - GROUP BY 절에서 사용하는 표현식(SUBSTR(PRODUCT_CODE, 1, 2))을 인덱스로 커버링하도록 설계
--   - 불필요한 데이터 스캔을 최소화하기 위해 필요한 컬럼만 SELECT 절에 포함

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N) 
--     -- 테이블 전체를 스캔하며 SUBSTR 함수와 COUNT 함수가 적용되어 선형 시간 복잡도
--   - 공간복잡도 : O(K) 
--     -- 그룹화된 결과를 저장하기 위한 공간 (K는 고유 카테고리 코드의 수)
-- -----------------------------------------------------------------------------------------
-- 최종 쿼리
-- -------------------------------------------------------------------------------------------

SELECT 
    SUBSTR(PRODUCT_CODE, 1, 2) AS CATEGORY,    -- 상품 코드의 앞 2자리 추출하여 카테고리로 사용
    COUNT(*) AS PRODUCTS                        -- 해당 카테고리의 상품 개수 계산
FROM 
    PRODUCT
GROUP BY
    SUBSTR(PRODUCT_CODE, 1, 2)                  -- 카테고리 코드별로 그룹화
ORDER BY 
    CATEGORY ASC;                                -- 카테고리 코드를 기준으로 오름차순 정렬