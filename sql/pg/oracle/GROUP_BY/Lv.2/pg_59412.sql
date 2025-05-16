-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/59412?language=oracle
-- 간단한 문제 설명 : 
--   - ANIMAL_OUTS 테이블에서 09:00부터 19:59까지의 입양 시각별 입양 건수를 조회
--   - 결과는 시간대 순으로 정렬하며, 시간은 앞의 0을 제거하여 출력

-- -----------------------------------------------------------------------------------------
-- 테이블 스키마 :
--   - 테이블명 : ANIMAL_OUTS
--     - ANIMAL_ID			VARCHAR(N)	FALSE	-- 동물의 아이디
--     - ANIMAL_TYPE		VARCHAR(N)	FALSE	-- 동물의 종류
--     - DATETIME			DATETIME	FALSE	-- 입양일시
--     - NAME				VARCHAR(N)	TRUE	-- 동물의 이름
--     - SEX_UPON_OUTCOME	VARCHAR(N)	FALSE	-- 성별 및 중성화 여부
-- -----------------------------------------------------------------------------------------
-- 해결 방법 설명 :
--   1. DATETIME 컬럼에서 시간을 추출하고 숫자형으로 변환
--   2. 09시부터 19시까지의 입양 건수를 집계
--   3. 시간대 순으로 오름차순 정렬
--
-- 사용한 SQL 문법 및 함수 설명 :
--   - TO_CHAR(DATETIME, 'HH24'): DATETIME에서 24시간 형식의 시간을 문자열로 추출
--   - TO_NUMBER(): 문자열을 숫자형으로 변환
--   - COUNT(*): 그룹별 행의 개수를 계산
--   - WHERE: 조건에 맞는 행을 필터링
--   - GROUP BY: 특정 컬럼으로 그룹화
--   - ORDER BY: 결과를 특정 컬럼 기준으로 정렬
--   - ASC: 오름차순 정렬 지정
--
-- 쿼리 최적화 방법 :
--   - DATETIME 컬럼에 인덱스를 생성하여 WHERE 절과 GROUP BY 절의 성능 향상
--     예시 인덱스 생성:
--       CREATE INDEX idx_animal_outs_datetime ON ANIMAL_OUTS(DATETIME);
-- -----------------------------------------------------------------------------------------
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N)
--     -- 테이블 전체를 스캔하며 조건에 맞는 행을 필터링하고 그룹화를 수행
--   - 공간복잡도 : O(K)
--     -- 그룹화된 결과를 저장하기 위한 공간 (K는 고유 시간대의 수)
-- -----------------------------------------------------------------------------------------
-- 최종 쿼리
-- -------------------------------------------------------------------------------------------

SELECT 
    TO_NUMBER(TO_CHAR(DATETIME, 'HH24')) AS HOUR,  -- 시간을 숫자형으로 추출하여 'HOUR'로 표시
    COUNT(*) AS COUNT  -- 각 시간대별 입양 건수를 계산
FROM 
    ANIMAL_OUTS
WHERE 
    TO_NUMBER(TO_CHAR(DATETIME, 'HH24')) BETWEEN 9 AND 19  -- 09:00부터 19:59까지의 시간대 선택
GROUP BY 
    TO_NUMBER(TO_CHAR(DATETIME, 'HH24'))  -- 시간대별로 그룹화
ORDER BY 
    HOUR ASC;  -- 시간대 순으로 오름차순 정렬