-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/131537
-- 간단한 문제 설명 : 
--   - 온라인/오프라인 판매 데이터 통합 조회
--   - 2022년 3월 데이터만 조회
--   - 판매일, 상품ID, 유저ID 순 정렬

-- 테이블 스키마 :
--   - 테이블명 : ONLINE_SALE
--     - ONLINE_SALE_ID INTEGER FALSE -- 온라인 판매 ID
--     - USER_ID INTEGER FALSE -- 회원 ID
--     - PRODUCT_ID INTEGER FALSE -- 상품 ID
--     - SALES_AMOUNT INTEGER FALSE -- 판매량
--     - SALES_DATE DATE FALSE -- 판매일
--
--   - 테이블명 : OFFLINE_SALE
--     - OFFLINE_SALE_ID INTEGER FALSE -- 오프라인 판매 ID
--     - PRODUCT_ID INTEGER FALSE -- 상품 ID
--     - SALES_AMOUNT INTEGER FALSE -- 판매량
--     - SALES_DATE DATE FALSE -- 판매일

-- 해결 방법 설명 :
--   1. 쿼리 작성 단계
--     - UNION ALL로 두 테이블 데이터 결합
--     - 오프라인 판매의 USER_ID를 NULL로 처리
--     - 날짜/상품ID/유저ID 순으로 정렬
--   2. 사용한 SQL 문법 및 함수 설명
--     - UNION ALL: 중복 제거 없이 데이터 결합
--     - TO_CHAR: 날짜 형식 변환
--     - ORDER BY: 정렬 조건 지정
--   3. 쿼리 최적화 방법
--     - SALES_DATE 인덱스 활용
--     - WHERE 절로 처리할 데이터 최소화

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N), N은 전체 판매 데이터 수
--   - 공간복잡도 : O(M), M은 3월 판매 데이터 수

SELECT 
    TO_CHAR(SALES_DATE, 'YYYY-MM-DD') AS SALES_DATE,
    PRODUCT_ID,
    USER_ID,
    SALES_AMOUNT
FROM 
    ONLINE_SALE
WHERE 
    TO_CHAR(SALES_DATE, 'YYYY-MM') = '2022-03'
    
UNION ALL

SELECT 
    TO_CHAR(SALES_DATE, 'YYYY-MM-DD') AS SALES_DATE,
    PRODUCT_ID,
    NULL AS USER_ID,
    SALES_AMOUNT
FROM 
    OFFLINE_SALE
WHERE 
    TO_CHAR(SALES_DATE, 'YYYY-MM') = '2022-03'
ORDER BY 1, 2, 3;