-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/164668
-- 간단한 문제 설명 : 
--   - USED_GOODS_BOARD와 USED_GOODS_USER 테이블을 활용하여 완료된 중고 거래의 총금액이 70만 원 이상인 사람의 회원 ID, 닉네임, 총거래금액을 조회
--   - 결과는 총거래금액을 기준으로 오름차순 정렬

-- 테이블 스키마 :
--   - 테이블명 : 
--     - USED_GOODS_BOARD
--       - BOARD_ID        VARCHAR(5)   NOT NULL  -- 게시글 ID
--       - WRITER_ID       VARCHAR(50)  NOT NULL  -- 작성자 ID
--       - TITLE           VARCHAR(100) NOT NULL  -- 게시글 제목
--       - CONTENTS        VARCHAR(1000) NOT NULL -- 게시글 내용
--       - PRICE           NUMBER       NOT NULL  -- 가격
--       - CREATED_DATE    DATE         NOT NULL  -- 작성일
--       - STATUS          VARCHAR(10)  NOT NULL  -- 거래상태
--       - VIEWS           NUMBER       NOT NULL  -- 조회수
--
--     - USED_GOODS_USER
--       - USER_ID          VARCHAR(50)  NOT NULL -- 회원 ID
--       - NICKNAME         VARCHAR(100) NOT NULL -- 닉네임
--       - CITY             VARCHAR(100) NOT NULL -- 시
--       - STREET_ADDRESS1  VARCHAR(100) NOT NULL -- 도로명 주소
--       - STREET_ADDRESS2  VARCHAR(100)  -- 상세 주소
--       - TLNO             VARCHAR(20) NOT NULL -- 전화번호

-- 해결 방법 설명 :
--   1. USED_GOODS_BOARD 테이블에서 STATUS가 'DONE'인 거래를 필터링
--   2. WRITER_ID를 기준으로 그룹화하여 각 사용자의 총 거래금액을 SUM(PRICE)으로 계산
--   3. 총 거래금액이 700,000 이상인 사용자만 HAVING 절을 사용하여 필터링
--   4. USED_GOODS_USER 테이블과 INNER JOIN하여 사용자 정보(USER_ID, NICKNAME)를 가져옴
--   5. 결과를 TOTAL_SALES 기준으로 오름차순 정렬

-- 사용한 SQL 문법 및 함수 설명 :
--   - INNER JOIN : 두 테이블을 WRITER_ID와 USER_ID로 결합하여 관련된 레코드를 가져옴
--   - WHERE 절 : STATUS가 'DONE'인 거래만 필터링
--   - GROUP BY : WRITER_ID와 NICKNAME을 기준으로 그룹화하여 각 사용자의 총 거래금액을 계산
--   - SUM() : 각 그룹의 PRICE 합계를 계산하여 총 거래금액을 구함
--   - HAVING 절 : 그룹화된 데이터 중 총 거래금액이 700,000 이상인 경우만 선택
--   - ORDER BY 절 : TOTAL_SALES를 기준으로 오름차순 정렬

-- 쿼리 최적화 방법 :
--   - USED_GOODS_BOARD 테이블의 WRITER_ID와 STATUS 컬럼에 인덱스를 생성하여 필터링 및 조인 성능 향상
--     예시:
--       CREATE INDEX idx_board_writer_status ON USED_GOODS_BOARD(WRITER_ID, STATUS);
--   - USED_GOODS_USER 테이블의 USER_ID 컬럼에 인덱스를 생성하여 조인 성능 향상
--     예시:
--       CREATE INDEX idx_user_id ON USED_GOODS_USER(USER_ID);
--   - 필요한 컬럼만 SELECT 절에 포함시켜 불필요한 데이터 스캔 최소화

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N), N은 USED_GOODS_BOARD 테이블의 총 행 수
--     -- STATUS가 'DONE'인 행을 필터링하고, WRITER_ID별로 그룹화하여 SUM을 계산
--   - 공간복잡도 : O(K), K는 70만 원 이상 거래한 사용자의 수
--     -- 그룹화된 결과를 저장하기 위한 공간 필요

SELECT 
    U.USER_ID AS USER_ID, 
    U.NICKNAME AS NICKNAME,
    SUM(B.PRICE) AS TOTAL_SALES
FROM 
    USED_GOODS_BOARD B
INNER JOIN 
    USED_GOODS_USER U 
    ON B.WRITER_ID = U.USER_ID
WHERE 
    B.STATUS = 'DONE'
GROUP BY 
    U.USER_ID,
    U.NICKNAME
HAVING 
    SUM(B.PRICE) >= 70*10000
ORDER BY 
    TOTAL_SALES ASC;