-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/132201?language=oracle
-- 간단한 문제 설명 : 
--   PATIENT 테이블에서 12세 이하인 여자 환자의 환자이름, 환자번호, 성별코드, 나이, 전화번호를 조회해야 합니다.
--   전화번호가 없는 경우 'NONE'으로 표시합니다.
--   결과는 나이를 기준으로 내림차순 정렬하고, 나이가 같다면 환자이름을 기준으로 오름차순 정렬합니다.
--
-- 테이블 스키마 :
--   - 테이블명 : PATIENT
--       PT_NO      VARCHAR(10)    NOT NULL   -- 환자번호
--       PT_NAME    VARCHAR(20)    NOT NULL   -- 환자이름
--       GEND_CD    VARCHAR(1)     NOT NULL   -- 성별코드
--       AGE        INTEGER         NOT NULL   -- 나이
--       TLNO       VARCHAR(50)      NULL      -- 전화번호
--
-- 해결 방법 설명 :
--   1. SELECT 절에서 필요한 컬럼(PT_NAME, PT_NO, GEND_CD, AGE, TLNO)을 선택합니다.
--   2. CASE 문을 사용하여 TLNO가 NULL인 경우 'NONE'으로 대체하고, 그렇지 않으면 기존 TLNO 값을 사용합니다.
--      - 오라클에서는 문자열 리터럴을 홑따옴표(')로 감싸야 합니다.
--   3. FROM 절에서 PATIENT 테이블을 지정합니다.
--   4. WHERE 절에서 GEND_CD가 'W'이고 AGE가 12 이하인 행을 필터링합니다.
--   5. ORDER BY 절에서 AGE를 기준으로 내림차순 정렬하고, AGE가 같은 경우 PT_NAME을 기준으로 오름차순 정렬합니다.
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N)
--       - N은 필터링된 환자 수입니다. ORDER BY 절에 의한 정렬 작업이 O(N log N)의 시간 복잡도를 가집니다.
--   - 공간복잡도 : O(N)
--       - 정렬된 결과를 저장하는 데 O(N)의 추가 공간이 필요합니다.

SELECT 
    PT_NAME, 
    PT_NO, 
    GEND_CD, 
    AGE, 
    CASE 
        WHEN TLNO IS NULL THEN 'NONE'  -- TLNO가 NULL인 경우 'NONE'으로 대체
        ELSE TLNO                      -- 그렇지 않은 경우 원래 TLNO 값을 사용
    END AS TLNO
FROM 
    PATIENT
WHERE 
    GEND_CD = 'W'     -- 성별 코드가 'W'인 환자 (여자)만 선택
    AND AGE <= 12     -- 나이가 12세 이하인 환자만 선택
ORDER BY 
    AGE DESC,         -- 나이를 기준으로 내림차순 정렬 (큰 나이부터 작은 나이 순)
    PT_NAME ASC;      -- 나이가 같은 경우 환자이름을 기준으로 오름차순 정렬 (A부터 Z 순)