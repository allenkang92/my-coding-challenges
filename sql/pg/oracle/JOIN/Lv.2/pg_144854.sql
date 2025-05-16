-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/144854
-- 간단한 문제 설명 : 
--   - BOOK 테이블과 AUTHOR 테이블을 조인하여 '경제' 카테고리에 속하는 도서의 도서 ID, 저자명, 출판일을 조회
--   - 출판일을 기준으로 오름차순 정렬
--   - 결과 컬럼명은 BOOK_ID, AUTHOR_NAME, PUBLISHED_DATE로 지정

-- -----------------------------------------------------------------------------------------
-- 테이블 스키마 :
--   - BOOK 테이블:
--     - BOOK_ID         INTEGER    NOT NULL  -- 도서 ID
--     - CATEGORY        VARCHAR(N) NOT NULL  -- 카테고리 (경제, 인문, 소설, 생활, 기술)
--     - AUTHOR_ID       INTEGER    NOT NULL  -- 저자 ID
--     - PRICE           INTEGER    NOT NULL  -- 판매가 (원)
--     - PUBLISHED_DATE  DATE       NOT NULL  -- 출판일
--
--   - AUTHOR 테이블:
--     - AUTHOR_ID      INTEGER    NOT NULL  -- 저자 ID
--     - AUTHOR_NAME    VARCHAR(N) NOT NULL  -- 저자명
-- -----------------------------------------------------------------------------------------
-- 해결 방법 설명:
--   1. BOOK 테이블과 AUTHOR 테이블을 AUTHOR_ID를 기준으로 INNER JOIN
--   2. '경제' 카테고리에 해당하는 도서를 필터링
--   3. 필요한 컬럼(BOOK_ID, AUTHOR_NAME, PUBLISHED_DATE)을 선택
--   4. PUBLISHED_DATE를 'YYYY-MM-DD' 형식으로 변환하여 출력
--   5. PUBLISHED_DATE를 기준으로 오름차순 정렬
--
-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT: 원하는 컬럼 선택
--   - INNER JOIN: 두 테이블을 AUTHOR_ID로 결합
--   - TO_CHAR: DATE 형식을 문자열로 변환
--   - WHERE: 조건에 맞는 행 필터링
--   - ORDER BY: 결과 정렬
--
-- 쿼리 최적화 방법 :
--   - BOOK 테이블의 AUTHOR_ID와 AUTHOR 테이블의 AUTHOR_ID에 인덱스를 생성하여 조인 성능 향상
--     예시 인덱스 생성:
--       CREATE INDEX idx_book_author_id ON BOOK(AUTHOR_ID);
--       CREATE INDEX idx_author_author_id ON AUTHOR(AUTHOR_ID);
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N) - 테이블 조인 및 필터링 연산
--   - 공간복잡도 : O(K) - 결과 저장 공간 (K는 '경제' 카테고리에 해당하는 도서의 수)
-- -------------------------------------------------------------------------------------------
-- 최종 쿼리
-- -------------------------------------------------------------------------------------------

SELECT 
    A.BOOK_ID AS BOOK_ID, 
    B.AUTHOR_NAME AS AUTHOR_NAME, 
    TO_CHAR(A.PUBLISHED_DATE, 'YYYY-MM-DD') AS PUBLISHED_DATE
FROM 
    BOOK A
INNER JOIN 
    AUTHOR B ON A.AUTHOR_ID = B.AUTHOR_ID
WHERE 
    A.CATEGORY = '경제'
ORDER BY 
    A.PUBLISHED_DATE ASC;

-- -------------------------------------------------------------------------------------------
-- 쿼리 오류 수정:
-- ORA-00920: invalid relational operator 오류는 주로 WHERE 절이나 JOIN 조건에서 잘못된 연산자 사용 시 발생합니다.
-- 현재 쿼리는 문법상 문제가 없으므로, 오류의 원인은 다음과 같을 수 있습니다:
--   1. 잘못된 따옴표 사용: '경제' 대신 다른 문자가 사용되었을 가능성
--   2. 테이블이나 컬럼 이름 오타
--   3. 추가적인 코드 오류 (예: 이전 라인에서 세미콜론 누락 등)
--
-- 제안된 수정 사항:
--   - ORDER BY 절에서 별칭 대신 실제 컬럼을 사용하도록 변경
--   - TO_CHAR 함수의 사용을 유지하거나 제거하여 테스트
--
-- 수정된 쿼리 예시:

SELECT 
    A.BOOK_ID, 
    B.AUTHOR_NAME, 
    TO_CHAR(A.PUBLISHED_DATE, 'YYYY-MM-DD') AS PUBLISHED_DATE
FROM 
    BOOK A
INNER JOIN 
    AUTHOR B ON A.AUTHOR_ID = B.AUTHOR_ID
WHERE 
    A.CATEGORY = '경제'
ORDER BY 
    A.PUBLISHED_DATE ASC;