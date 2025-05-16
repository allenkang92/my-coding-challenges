-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/144855?language=oracle
-- 간단한 문제 설명 : 
--   - BOOK과 BOOK_SALES 테이블을 활용하여 2022년 1월의 카테고리 별 도서 판매량을 합산
--   - 카테고리명과 총 판매량을 출력하며, 카테고리명을 기준으로 오름차순 정렬

-- 테이블 스키마 :
--   - 테이블명 : 
--     - BOOK
--       - BOOK_ID        INTEGER      NOT NULL  -- 도서 ID
--       - CATEGORY       VARCHAR(N)   NOT NULL  -- 카테고리 (경제, 인문, 소설, 생활, 기술)
--       - AUTHOR_ID      INTEGER      NOT NULL  -- 저자 ID
--       - PRICE          INTEGER      NOT NULL  -- 판매가 (원)
--       - PUBLISHED_DATE DATE         NOT NULL  -- 출판일
--     - BOOK_SALES
--       - BOOK_ID    INTEGER      NOT NULL  -- 도서 ID
--       - SALES_DATE DATE         NOT NULL  -- 판매일
--       - SALES      INTEGER      NOT NULL  -- 판매량

-- 해결 방법 설명 :
--   1. BOOK 테이블과 BOOK_SALES 테이블을 BOOK_ID로 INNER JOIN
--   2. SALES_DATE가 2022년 1월인 데이터 필터링
--   3. CATEGORY 별로 SALES 합산
--   4. 결과를 CATEGORY 기준 오름차순 정렬

-- 사용한 SQL 문법 및 함수 설명 :
--   - INNER JOIN : 두 테이블을 BOOK_ID로 결합
--   - TO_CHAR : SALES_DATE를 'YYYY-MM' 형식으로 변환
--   - GROUP BY : CATEGORY 별로 그룹화
--   - SUM() : SALES 합산
--   - ORDER BY : CATEGORY 오름차순 정렬

-- 쿼리 최적화 방법 :
--   - BOOK_SALES 테이블의 SALES_DATE에 인덱스 생성
--   - BOOK 테이블의 BOOK_ID에 인덱스 생성

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N), N은 BOOK_SALES 테이블의 행 수
--   - 공간복잡도 : O(K), K는 카테고리의 수

SELECT 
    A.CATEGORY AS CATEGORY, 
    SUM(B.SALES) AS TOTAL_SALES
FROM 
    BOOK A
INNER JOIN 
    BOOK_SALES B 
    ON A.BOOK_ID = B.BOOK_ID
WHERE 
    TO_CHAR(B.SALES_DATE, 'YYYY-MM') = '2022-01'
GROUP BY 
    A.CATEGORY
ORDER BY 
    CATEGORY ASC;