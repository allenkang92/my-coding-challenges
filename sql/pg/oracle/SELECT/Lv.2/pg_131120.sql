-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131120?language=oracle
-- 간단한 문제 설명 : 
--   - MEMBER_PROFILE 테이블에서 생일이 3월인 여성 회원의 ID, 이름, 성별 및 생년월일을 조회
--   - 전화번호(TLNO)가 NULL인 경우 제외
--   - 결과는 MEMBER_ID 기준 오름차순 정렬

-- -----------------------------------------------------------------------------------------
-- 테이블 스키마 (MEMBER_PROFILE):
--   - MEMBER_ID      VARCHAR(100)  NOT NULL  -- 회원 ID
--   - MEMBER_NAME    VARCHAR(50)   NOT NULL  -- 회원 이름
--   - TLNO           VARCHAR(50)   TRUE      -- 회원 연락처 (NULL 가능)
--   - GENDER         VARCHAR(1)    TRUE      -- 성별 ('W' 또는 'M', NULL 가능)
--   - DATE_OF_BIRTH  DATE          TRUE      -- 생년월일 (NULL 가능)
-- -----------------------------------------------------------------------------------------
-- 해결 방법 설명:
--   1. SELECT 절에서 필요한 컬럼(MEMBER_ID, MEMBER_NAME, GENDER, DATE_OF_BIRTH)을 선택
--   2. WHERE 절에서 GENDER = 'W' 조건으로 여성 회원 필터링
--   3. AND TLNO IS NOT NULL 조건으로 전화번호가 있는 회원만 선택
--   4. AND SUBSTR(TO_CHAR(DATE_OF_BIRTH, 'YYYY-MM-DD'), 6, 2) = '03' 조건으로 생일이 3월인 회원 필터링
--   5. ORDER BY 절을 사용하여 MEMBER_ID를 기준으로 오름차순 정렬
--
-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT: 원하는 컬럼을 선택
--   - TO_CHAR: DATE 타입을 문자열로 변환
--   - SUBSTR: 문자열의 일부를 추출
--   - WHERE: 조건에 맞는 행을 필터링
--   - ORDER BY: 결과를 특정 컬럼 기준으로 정렬
--
-- 쿼리 최적화 방법 :
--   - GENDER, TLNO, DATE_OF_BIRTH 컬럼에 인덱스를 생성하면 WHERE 절의 조건 검색 속도를 향상시킬 수 있음
--   - DATE_OF_BIRTH 컬럼에 인덱스를 생성하면 생일 기반 필터링 성능이 개선될 수 있음
--   - 인덱스는 데이터베이스의 조회 속도를 크게 향상시킬 수 있는 중요한 요소이지만, 너무 많은 인덱스는 쓰기 성능을 저하시킬 수 있으므로 주의가 필요함
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N) - 테이블 전체 스캔 후 조건 필터링 및 정렬
--   - 공간복잡도 : O(N) - 결과 집합 저장 공간

-- -------------------------------------------------------------------------------------------
-- 최종 쿼리
-- -------------------------------------------------------------------------------------------

SELECT 
    MEMBER_ID,                                         -- 회원 ID
    MEMBER_NAME,                                       -- 회원 이름
    GENDER,                                            -- 성별
    TO_CHAR(DATE_OF_BIRTH, 'YYYY-MM-DD') AS DATE_OF_BIRTH  -- 생년월일을 'YYYY-MM-DD' 형식으로 변환
FROM 
    MEMBER_PROFILE                                     -- 데이터 소스 테이블
WHERE 
    GENDER = 'W'                                       -- 여성 회원만 선택
    AND TLNO IS NOT NULL                              -- 전화번호가 있는 회원만 선택
    AND SUBSTR(TO_CHAR(DATE_OF_BIRTH, 'YYYY-MM-DD'), 6, 2) = '03'  -- 생일이 3월인 회원만 선택
ORDER BY 
    MEMBER_ID ASC;                                     -- MEMBER_ID 기준 오름차순 정렬

-- -------------------------------------------------------------------------------------------
-- 추가 최적화: EXTRACT 함수를 사용한 생월 추출 방법
-- -------------------------------------------------------------------------------------------

-- EXTRACT 함수를 사용하여 생월을 직접 추출할 수 있습니다. 이는 가독성을 높이고, 성능을 약간 향상시킬 수 있습니다.

SELECT 
    MEMBER_ID,                                        
    MEMBER_NAME,                                      
    GENDER,                                            
    TO_CHAR(DATE_OF_BIRTH, 'YYYY-MM-DD') AS DATE_OF_BIRTH 
FROM 
    MEMBER_PROFILE                                    
WHERE 
    GENDER = 'W'                                      
    AND TLNO IS NOT NULL                             
    AND EXTRACT(MONTH FROM DATE_OF_BIRTH) = 3        -- 생월이 3월인 회원만 선택
ORDER BY 
    MEMBER_ID ASC;                                    

-- -------------------------------------------------------------------------------------------
-- 대체 함수 사용: NVL 함수를 사용하여 NULL 처리
-- -------------------------------------------------------------------------------------------

-- 만약 생년월일이 NULL인 경우를 추가로 처리해야 한다면, NVL 함수를 사용할 수 있습니다.

SELECT 
    MEMBER_ID,                                        
    MEMBER_NAME,                                      
    GENDER,                                            
    NVL(TO_CHAR(DATE_OF_BIRTH, 'YYYY-MM-DD'), 'Unknown') AS DATE_OF_BIRTH 
FROM 
    MEMBER_PROFILE                                    
WHERE 
    GENDER = 'W'                                      
    AND TLNO IS NOT NULL                             
    AND EXTRACT(MONTH FROM DATE_OF_BIRTH) = 3        
ORDER BY 
    MEMBER_ID ASC;                                    

-- -------------------------------------------------------------------------------------------
-- 인덱스 생성 예시
-- -------------------------------------------------------------------------------------------

-- 성능 최적화를 위한 인덱스 생성 예시입니다.

-- GENDER 컬럼에 인덱스 생성
CREATE INDEX idx_gender ON MEMBER_PROFILE(GENDER);

-- TLNO 컬럼에 인덱스 생성
CREATE INDEX idx_tlno ON MEMBER_PROFILE(TLNO);

-- DATE_OF_BIRTH 컬럼에 인덱스 생성
CREATE INDEX idx_dob ON MEMBER_PROFILE(DATE_OF_BIRTH);

-- -------------------------------------------------------------------------------------------