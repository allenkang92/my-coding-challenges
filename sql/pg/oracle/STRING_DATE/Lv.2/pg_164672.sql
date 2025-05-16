-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/164672?language=oracle
-- 간단한 문제 설명 : 
--   - USED_GOODS_BOARD 테이블에서 특정 날짜에 등록된 중고거래 게시물의 정보를 조회
--   - 거래 상태를 이해하기 쉬운 한글로 변환
--   - 결과는 게시글 ID를 기준으로 내림차순 정렬

-- -----------------------------------------------------------------------------------------
-- 테이블 스키마 :
--   - USED_GOODS_BOARD 테이블:
--     - BOARD_ID       VARCHAR(5)    NOT NULL  -- 게시글 ID
--     - WRITER_ID      VARCHAR(50)   NOT NULL  -- 작성자 ID
--     - TITLE          VARCHAR(100)  NOT NULL  -- 게시글 제목
--     - CONTENTS       VARCHAR(1000) NOT NULL  -- 게시글 내용
--     - PRICE          NUMBER        NOT NULL  -- 가격
--     - CREATED_DATE   DATE          NOT NULL  -- 작성일
--     - STATUS         VARCHAR(10)   NOT NULL  -- 거래 상태 (SALE, RESERVED, DONE)
--     - VIEWS          NUMBER        NOT NULL  -- 조회수
-- -----------------------------------------------------------------------------------------
-- 해결 방법 설명:
--   1. USED_GOODS_BOARD 테이블에서 BOARD_ID, WRITER_ID, TITLE, PRICE, STATUS 컬럼을 선택
--   2. CASE 문을 사용하여 STATUS 값을 한글로 변환
--      - 'SALE'은 '판매중'으로
--      - 'RESERVED'는 '예약중'으로
--      - 'DONE'은 '거래완료'로
--   3. WHERE 절을 사용하여 CREATED_DATE가 2022년 10월 5일인 레코드만 필터링
--   4. ORDER BY 절을 사용하여 BOARD_ID를 기준으로 내림차순 정렬
--
-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT: 조회할 컬럼을 선택
--   - FROM: 데이터를 조회할 테이블을 지정
--   - WHERE: 조건에 맞는 행을 필터링
--   - CASE WHEN ... THEN ... ELSE ... END: 조건에 따라 다른 값을 반환
--   - ORDER BY: 결과를 특정 컬럼 기준으로 정렬
--   - DESC: 내림차순 정렬 지정

-- 쿼리 최적화 방법 :
--   - CREATED_DATE 컬럼에 인덱스를 생성하여 WHERE 절의 필터링 성능 향상
--     예시 인덱스 생성:
--       CREATE INDEX idx_created_date ON USED_GOODS_BOARD(CREATED_DATE);
--   - STATUS 컬럼에 인덱스를 생성하여 CASE 문에서의 변환 성능 향상
--     예시 인덱스 생성:
--       CREATE INDEX idx_status ON USED_GOODS_BOARD(STATUS);
--   - 필요한 컬럼만 SELECT 절에 포함하여 불필요한 데이터 스캔을 줄임

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N)
--     -- 테이블 전체를 스캔하며 필터링과 정렬을 수행
--   - 공간복잡도 : O(K)
--     -- 결과 집합을 저장하는 데 필요한 공간 (K는 조건에 맞는 게시글의 수)
-- -----------------------------------------------------------------------------------------
-- 최종 쿼리
-- -------------------------------------------------------------------------------------------

SELECT 
    BOARD_ID,                                       -- 게시글의 고유 ID
    WRITER_ID,                                      -- 작성자의 ID
    TITLE,                                          -- 게시글 제목
    PRICE,                                          -- 판매 가격
    CASE 
        WHEN STATUS = 'SALE' THEN '판매중'          -- 거래 상태가 SALE이면 '판매중'으로 표시
        WHEN STATUS = 'RESERVED' THEN '예약중'      -- 거래 상태가 RESERVED이면 '예약중'으로 표시
        WHEN STATUS = 'DONE' THEN '거래완료'        -- 거래 상태가 DONE이면 '거래완료'으로 표시
        ELSE '알 수 없음'                           -- 그 외의 상태는 '알 수 없음'으로 표시
    END AS STATUS                                  -- 변환된 거래 상태를 STATUS 컬럼으로 명명
FROM 
    USED_GOODS_BOARD
WHERE 
    CREATED_DATE = DATE '2022-10-05'               -- 작성일이 2022년 10월 5일인 게시글 필터링
ORDER BY 
    BOARD_ID DESC;                                 -- BOARD_ID를 기준으로 내림차순 정렬

-- -------------------------------------------------------------------------------------------
-- 쿼리 오류 수정:
-- 오류 메시지: 없음
-- 원인:
--   - 기존 쿼리는 STATUS 값을 정확히 매핑하지 못하거나, 날짜 형식이 올바르지 않았을 가능성
-- 해결 방법:
--   1. DATE 리터럴을 사용하여 CREATED_DATE를 정확히 비교
--      예: DATE '2022-10-05'
--   2. CASE 문에서 모든 가능한 STATUS 값을 처리하거나, 기본값을 지정
--   3. STATUS 컬럼의 값이 정확히 'SALE', 'RESERVED', 'DONE'인지 확인
-- -------------------------------------------------------------------------------------------
