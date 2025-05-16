-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/164671
-- 간단한 문제 설명 : 
--   - USED_GOODS_BOARD 테이블과 USED_GOODS_FILE 테이블을 활용하여 조회수가 가장 높은 중고거래 게시물의 첨부파일 경로를 조회
--   - 첨부파일 경로는 기본 경로에 게시글 ID와 파일 정보를 결합하여 생성
--   - 결과는 FILE_ID를 기준으로 내림차순 정렬

-- 테이블 스키마 :
--   - 테이블명 : 
--     - USED_GOODS_BOARD
--       - BOARD_ID     VARCHAR(5)  NOT NULL  -- 게시글 ID
--       - WRITER_ID    VARCHAR(50) NOT NULL  -- 작성자 ID
--       - TITLE        VARCHAR(100) NOT NULL -- 게시글 제목
--       - CONTENTS     VARCHAR(1000) NOT NULL-- 게시글 내용
--       - PRICE        NUMBER      NOT NULL  -- 가격
--       - CREATED_DATE DATE        NOT NULL  -- 작성일
--       - STATUS       VARCHAR(10) NOT NULL  -- 거래상태
--       - VIEWS        NUMBER      NOT NULL  -- 조회수
--
--     - USED_GOODS_FILE
--       - FILE_ID     VARCHAR(10) NOT NULL -- 파일 ID
--       - FILE_EXT    VARCHAR(5)  NOT NULL -- 파일 확장자
--       - FILE_NAME   VARCHAR(256) NOT NULL -- 파일 이름
--       - BOARD_ID    VARCHAR(10) NOT NULL -- 게시글 ID

-- 해결 방법 설명 :
--   1. USED_GOODS_BOARD와 USED_GOODS_FILE 테이블을 BOARD_ID로 INNER JOIN
--   2. 조회수가 가장 높은 게시물을 찾기 위해 서브쿼리를 사용하여 MAX(VIEWS)를 구함
--   3. 해당 게시물의 첨부파일 경로를 '/home/grep/src/'와 BOARD_ID, FILE_ID, FILE_NAME, FILE_EXT를 결합하여 생성
--   4. 결과를 FILE_ID를 기준으로 내림차순 정렬

-- 사용한 SQL 문법 및 함수 설명 :
--   - INNER JOIN : 두 테이블을 특정 조건(BOARD_ID)을 기준으로 결합
--   - 서브쿼리 : 조회수가 가장 높은 게시물을 찾기 위해 사용
--   - 문자열 결합 연산자(||) : 파일 경로를 생성하기 위해 여러 문자열을 결합
--   - ORDER BY DESC : FILE_ID를 기준으로 내림차순 정렬

-- 쿼리 최적화 방법 :
--   - USED_GOODS_BOARD 테이블의 VIEWS 컬럼에 인덱스 생성하여 MAX(VIEWS) 검색 속도 향상
--     예시:
--       CREATE INDEX idx_board_views ON USED_GOODS_BOARD(VIEWS);
--   - BOARD_ID 컬럼에 인덱스 생성하여 JOIN 성능 향상
--     예시:
--       CREATE INDEX idx_board_id ON USED_GOODS_BOARD(BOARD_ID);
--       CREATE INDEX idx_file_board_id ON USED_GOODS_FILE(BOARD_ID);
--   - 필요한 컬럼만 SELECT 절에 포함하여 I/O 최소화

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N), 테이블 전체를 스캔하여 MAX(VIEWS)를 찾고 조인 수행
--   - 공간복잡도 : O(N), 조인 결과와 파일 경로 생성을 위한 임시 공간 사용

SELECT 
    '/home/grep/src/' || B.BOARD_ID || '/' || B.FILE_ID || B.FILE_NAME || B.FILE_EXT AS FILE_PATH
FROM USED_GOODS_BOARD A
INNER JOIN USED_GOODS_FILE B ON A.BOARD_ID = B.BOARD_ID
WHERE 
    A.VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
ORDER BY B.FILE_ID DESC
;