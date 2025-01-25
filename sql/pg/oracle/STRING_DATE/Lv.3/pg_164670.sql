-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/164670
-- 간단한 문제 설명 : 
--   - USED_GOODS_BOARD 테이블과 USED_GOODS_USER 테이블을 활용하여 중고 거래 게시물을 3건 이상 등록한 사용자의 정보 조회
--   - 조회 항목: 사용자 ID, 닉네임, 전체 주소, 전화번호
--   - 전체 주소는 시, 도로명 주소, 상세 주소를 합친 형태
--   - 전화번호는 xxx-xxxx-xxxx 형식으로 하이픈 삽입
--   - 결과는 사용자 ID를 기준으로 내림차순 정렬

-- 테이블 스키마 :
--   - 사용 테이블명 : 
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
--     - USED_GOODS_USER
--       - USER_ID          VARCHAR(50) NOT NULL  -- 회원 ID
--       - NICKNAME         VARCHAR(100) NOT NULL -- 닉네임
--       - CITY             VARCHAR(100) NOT NULL -- 시
--       - STREET_ADDRESS1  VARCHAR(100) NOT NULL -- 도로명 주소
--       - STREET_ADDRESS2  VARCHAR(100)          -- 상세 주소
--       - TLNO             VARCHAR(20) NOT NULL  -- 전화번호

-- 해결 방법 설명 :
--   1. USED_GOODS_BOARD와 USED_GOODS_USER 테이블을 WRITER_ID와 USER_ID를 기준으로 INNER JOIN
--   2. GROUP BY 절을 사용하여 각 사용자가 작성한 게시글 수를 집계
--   3. HAVING 절을 사용하여 게시글 수가 3건 이상인 사용자만 필터링
--   4. SELECT 절에서 필요한 사용자 정보와 조건에 맞게 전화번호 및 전체주소 포맷팅
--   5. ORDER BY 절을 사용하여 USER_ID 기준 내림차순 정렬

-- 사용한 SQL 문법 및 함수 설명 :
--   - INNER JOIN : 두 테이블을 특정 조건(WRITER_ID = USER_ID)으로 결합
--   - GROUP BY : WRITER_ID를 기준으로 그룹화하여 각 사용자의 게시글 수를 집계
--   - HAVING COUNT(A.BOARD_ID) >= 3 : 게시글 수가 3건 이상인 그룹만 선택
--   - CONCAT 연산자(||) : 여러 문자열을 결합하여 전체주소와 전화번호 형식 지정
--   - SUBSTR 함수 : 전화번호의 특정 부분을 추출하여 하이픈 삽입
--   - DISTINCT : 중복된 행을 제거 (필요 시 사용)
--   - ORDER BY : 결과를 특정 컬럼(USER_ID)을 기준으로 정렬

-- 쿼리 최적화 방법 (인덱스 사용, 조인 방식 등) :
--   - USED_GOODS_BOARD 테이블의 WRITER_ID 컬럼과 USED_GOODS_USER 테이블의 USER_ID 컬럼에 인덱스 생성
--     예시:
--       CREATE INDEX idx_board_writer_id ON USED_GOODS_BOARD(WRITER_ID);
--       CREATE INDEX idx_user_id ON USED_GOODS_USER(USER_ID);
--   - 필요한 컬럼만 SELECT 절에 포함하여 데이터 스캔량 최소화
--   - JOIN 절에서 사용하는 컬럼에 인덱스를 적용하여 조인 성능 향상

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N), N은 USED_GOODS_BOARD 테이블의 총 행 수
--     -- 테이블 전체를 스캔한 후 조인 및 그룹화 수행
--   - 공간복잡도 : O(K), K는 조건을 만족하는 사용자 수
--     -- 그룹화된 결과를 저장하기 위한 임시 공간 필요

SELECT
    A.WRITER_ID AS USER_ID,
    B.NICKNAME,
    B.CITY || ' ' || B.STREET_ADDRESS1 || ' ' || B.STREET_ADDRESS2 AS 전체주소,
    SUBSTR(B.TLNO, 1, 3) || '-' || SUBSTR(B.TLNO, 4, 4) || '-' || SUBSTR(B.TLNO, 8, 4) AS 전화번호
FROM USED_GOODS_BOARD A
INNER JOIN USED_GOODS_USER B ON A.WRITER_ID = B.USER_ID
GROUP BY
    A.WRITER_ID,
    B.NICKNAME,
    B.CITY,
    B.STREET_ADDRESS1,
    B.STREET_ADDRESS2,
    B.TLNO
HAVING COUNT(A.BOARD_ID) >= 3
ORDER BY USER_ID DESC;