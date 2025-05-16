-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/144853?language=oracle
-- 간단한 문제 설명 : 
--   2021년에 출판된 인문 카테고리 도서의 ID와 출판일을 출판일 오름차순으로 조회
--
-- 테이블 스키마 :
--   - 테이블명 : BOOK
--   - 컬럼정보:
--       BOOK_ID INTEGER        NOT NULL  -- 도서 ID
--       CATEGORY VARCHAR(N)    NOT NULL  -- 카테고리
--       AUTHOR_ID INTEGER      NOT NULL  -- 저자 ID
--       PRICE INTEGER         NOT NULL  -- 판매가
--       PUBLISHED_DATE DATE    NOT NULL  -- 출판일
--
-- 해결 방법 설명 :
--   1. TO_CHAR 함수로 날짜를 'YYYY-MM-DD' 형식으로 변환
--   2. WHERE 절에서 CATEGORY = '인문'과 TO_CHAR(PUBLISHED_DATE, 'YYYY') = '2021' 조건 사용
--   3. ORDER BY로 출판일 오름차순 정렬
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N) - ORDER BY로 인한 정렬
--   - 공간복잡도 : O(K) - K는 조건을 만족하는 도서 수

SELECT 
    BOOK_ID, 
    TO_CHAR(PUBLISHED_DATE, 'YYYY-MM-DD') AS PUBLISHED_DATE
FROM 
    BOOK
WHERE 
    CATEGORY = '인문' 
    AND TO_CHAR(PUBLISHED_DATE, 'YYYY') = '2021'
ORDER BY 
    PUBLISHED_DATE ASC;