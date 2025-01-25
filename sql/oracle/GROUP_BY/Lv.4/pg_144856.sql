-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/144856
-- 간단한 문제 설명 : 
--   - 2022년 1월 도서 판매 데이터 기준 저자/카테고리별 매출액 집계
--   - 저자ID 오름차순, 카테고리 내림차순 정렬

-- 테이블 스키마 :
--   - 테이블명 : BOOK
--     - BOOK_ID INTEGER FALSE -- 도서 ID
--     - CATEGORY VARCHAR(N) FALSE -- 카테고리
--     - AUTHOR_ID INTEGER FALSE -- 저자 ID
--     - PRICE INTEGER FALSE -- 판매가
--     - PUBLISHED_DATE DATE FALSE -- 출판일
--
--   - 테이블명 : AUTHOR
--     - AUTHOR_ID INTEGER FALSE -- 저자 ID
--     - AUTHOR_NAME VARCHAR(N) FALSE -- 저자명
--
--   - 테이블명 : BOOK_SALES
--     - BOOK_ID INTEGER FALSE -- 도서 ID
--     - SALES_DATE DATE FALSE -- 판매일
--     - SALES INTEGER FALSE -- 판매량

-- 해결 방법 설명 :
--   1. 쿼리 작성 단계
--     - 3개 테이블 INNER JOIN
--     - 2022년 1월 데이터 필터링
--     - 저자/카테고리별 매출액 집계
--     - 정렬 조건 적용
--
--   2. 사용한 SQL 문법 및 함수 설명
--     - JOIN: 테이블 결합
--     - TO_CHAR: 날짜 형식 변환
--     - SUM: 매출액 합계 계산
--     - GROUP BY: 저자/카테고리별 집계
--
--   3. 쿼리 최적화 방법
--     - 인덱스: BOOK_SALES.SALES_DATE에 인덱스 생성
--     - JOIN 순서: BOOK → AUTHOR → BOOK_SALES

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N), N은 판매 데이터 수
--   - 공간복잡도 : O(M), M은 저자*카테고리 조합 수

SELECT 
    A.AUTHOR_ID, 
    B.AUTHOR_NAME, 
    A.CATEGORY,
    SUM(C.SALES * A.PRICE) AS TOTAL_SALES
FROM 
    BOOK A 
JOIN 
    AUTHOR B ON A.AUTHOR_ID = B.AUTHOR_ID
JOIN 
    BOOK_SALES C ON A.BOOK_ID = C.BOOK_ID
WHERE 
    TO_CHAR(C.SALES_DATE, 'YYYY-MM') = '2022-01'
GROUP BY 
    A.AUTHOR_ID, 
    B.AUTHOR_NAME,
    A.CATEGORY
ORDER BY 
    A.AUTHOR_ID ASC, 
    A.CATEGORY DESC;