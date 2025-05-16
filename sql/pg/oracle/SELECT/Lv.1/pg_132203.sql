-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/132203?language=oracle
-- 간단한 문제 설명 : 
--   DOCTOR 테이블에서 진료과 코드가 흉부외과(CS) 또는 일반외과(GS)인 의사의 이름, 의사ID, 진료과 코드, 고용일자를 조회해야 합니다.
--   결과는 고용일자를 기준으로 내림차순 정렬하고, 고용일자가 같다면 의사 이름을 기준으로 오름차순 정렬합니다.
--
-- 테이블 스키마 :
--   - 테이블명 : DOCTOR
--       DR_NAME    VARCHAR(20)   NOT NULL  -- 의사 이름
--       DR_ID      VARCHAR(10)   NOT NULL  -- 의사 ID
--       LCNS_NO    VARCHAR(30)   NOT NULL  -- 면허번호
--       HIRE_YMD   DATE          NOT NULL  -- 고용일자
--       MCDP_CD    VARCHAR(6)    NULL      -- 진료과 코드
--       TLNO       VARCHAR(50)    NULL      -- 전화번호
--
-- 해결 방법 설명 :
--   1. DOCTOR 테이블에서 진료과 코드(MCDP_CD)가 'CS' 또는 'GS'인 의사들을 필터링합니다.
--   2. 필요한 컬럼(DR_NAME, DR_ID, MCDP_CD, HIRE_YMD)을 SELECT 절에 지정합니다.
--   3. HIRE_YMD 컬럼의 날짜 포맷을 'YYYY-MM-DD' 형태로 변환하여 출력합니다.
--      - TO_CHAR 함수를 사용하여 DATE 타입을 원하는 문자열 형식으로 변환합니다.
--   4. ORDER BY 절을 사용하여 먼저 HIRE_YMD를 기준으로 내림차순 정렬하고, 
--      동일한 고용일자 내에서는 DR_NAME을 기준으로 오름차순 정렬합니다.
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N)
--       - N은 필터링된 의사들의 수이며, ORDER BY 절로 인한 정렬 작업의 시간 복잡도는 O(N log N)입니다.
--   - 공간복잡도 : O(N)
--       - 결과 집합을 저장하는 데 O(N)의 공간이 필요합니다.

SELECT 
    DR_NAME, 
    DR_ID, 
    MCDP_CD, 
    TO_CHAR(HIRE_YMD, 'YYYY-MM-DD') AS HIRE_YMD
FROM 
    DOCTOR
WHERE 
    MCDP_CD = 'CS' 
    OR MCDP_CD = 'GS'
ORDER BY 
    HIRE_YMD DESC,  -- 고용일자를 기준으로 내림차순 정렬 (최근 고용일자 순)
    DR_NAME ASC;     -- 고용일자가 동일한 경우 의사 이름을 기준으로 오름차순 정렬