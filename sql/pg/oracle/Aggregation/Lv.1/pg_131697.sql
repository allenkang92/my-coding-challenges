-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131697?language=oracle
-- 간단한 문제 설명 : 
--   PRODUCT 테이블에서 가장 높은 판매가를 조회합니다.
--
-- 테이블 스키마 :
--   - 테이블명 : PRODUCT
--   - 컬럼정보:
--       PRODUCT_ID INTEGER     NOT NULL  -- 상품 ID
--       PRODUCT_CODE VARCHAR(8) NOT NULL  -- 상품코드 (8자리)
--       PRICE INTEGER         NOT NULL  -- 판매가
--
-- 해결 방법 설명 :
--   1. MAX 함수를 사용하여 PRICE 컬럼의 최댓값 조회
--   2. 별칭을 MAX_PRICE로 지정
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N) - 전체 데이터 스캔
--   - 공간복잡도 : O(1) - 단일 결과값만 저장

SELECT 
    MAX(PRICE) AS MAX_PRICE  -- PRICE 컬럼의 최댓값을 MAX_PRICE로 조회
FROM 
    PRODUCT;