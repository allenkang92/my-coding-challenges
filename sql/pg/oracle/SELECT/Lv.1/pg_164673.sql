-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/164673?language=oracle
-- 간단한 문제 설명 :
--   USED_GOODS_BOARD와 USED_GOODS_REPLY 테이블에서
--   2022년 10월에 작성된 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일을 조회.
--   결과는 댓글 작성일을 기준으로 오름차순 정렬, 동일 날짜 시 게시글 제목을 기준으로 추가 오름차순 정렬.
--
-- 테이블 스키마 :
--   - 테이블명 : USED_GOODS_BOARD
--       BOARD_ID VARCHAR(5),
--       WRITER_ID VARCHAR(50),
--       TITLE VARCHAR(100),
--       CONTENTS VARCHAR(1000),
--       PRICE NUMBER,
--       CREATED_DATE DATE,
--       STATUS VARCHAR(10),
--       VIEWS NUMBER
--   - 테이블명 : USED_GOODS_REPLY
--       REPLY_ID VARCHAR(10),
--       BOARD_ID VARCHAR(5),
--       WRITER_ID VARCHAR(50),
--       CONTENTS VARCHAR(1000),
--       CREATED_DATE DATE
--
-- 해결 방법 설명 :
--   1. USED_GOODS_BOARD(A)와 USED_GOODS_REPLY(B)를 BOARD_ID 기준 INNER JOIN
--   2. 댓글 작성일(B.CREATED_DATE)이 2022년 10월인 데이터만 필터링
--   3. SELECT 절에서 TO_CHAR로 날짜 포맷을 'YYYY-MM-DD' 형태로 변환
--   4. ORDER BY로 댓글 작성일 오름차순, 동일 날짜 시 게시글 제목 오름차순
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N) (ORDER BY에 의한 정렬 비용)
--   - 공간복잡도 : O(N) (조인 및 정렬된 결과 저장)

SELECT
    A.TITLE,
    A.BOARD_ID,
    B.REPLY_ID,
    B.WRITER_ID,
    B.CONTENTS,
    TO_CHAR(B.CREATED_DATE, 'YYYY-MM-DD') AS CREATED_DATE
FROM 
    USED_GOODS_BOARD A
JOIN 
    USED_GOODS_REPLY B
    ON A.BOARD_ID = B.BOARD_ID
WHERE
    TO_CHAR(B.CREATED_DATE, 'YYYY-MM') = '2022-10'
ORDER BY
    B.CREATED_DATE ASC,
    A.TITLE ASC;