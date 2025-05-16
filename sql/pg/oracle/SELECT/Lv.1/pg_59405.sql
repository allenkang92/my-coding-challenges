-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/59405?language=oracle
-- 간단한 문제 설명 : 
--   동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 문제입니다.
--
-- 테이블 스키마 :
--   - 테이블명 : ANIMAL_INS
--   - 컬럼정보:
--       ANIMAL_ID VARCHAR(N)    NOT NULL  -- 동물 아이디
--       ANIMAL_TYPE VARCHAR(N)  NOT NULL  -- 생물 종
--       DATETIME DATETIME       NOT NULL  -- 보호 시작일
--       INTAKE_CONDITION VARCHAR(N) NOT NULL  -- 보호 시작시 상태
--       NAME VARCHAR(N)         TRUE      -- 이름
--       SEX_UPON_INTAKE VARCHAR(N) NOT NULL  -- 성별 및 중성화 여부
--
-- 해결 방법 설명 :
--   1. Oracle 12c 이상: FETCH FIRST ROW ONLY 사용
--      - 표준 SQL 문법
--      - 명시적이고 가독성이 좋음
--   2. 모든 Oracle 버전: ROWNUM 사용
--      - 행 번호를 기준으로 필터링
--      - 레거시 시스템 호환성 좋음
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N)
--       - ORDER BY로 인한 정렬 비용
--   - 공간복잡도 : O(1)
--       - 단일 결과값만 저장

-- 방법 1: FETCH FIRST ROW ONLY 사용
-- DATETIME으로 정렬 후 첫 번째 행만 가져옴
SELECT 
    NAME  -- 동물 이름만 조회
FROM 
    ANIMAL_INS
ORDER BY 
    DATETIME ASC  -- 보호 시작일 오름차순 정렬
FETCH FIRST ROW ONLY;  -- 첫 번째 행만 선택

-- 방법 2: ROWNUM 사용
-- Oracle의 가상 컬럼인 ROWNUM 활용
SELECT 
    NAME  -- 동물 이름만 조회
FROM 
    ANIMAL_INS
WHERE 
    ROWNUM = 1  -- 첫 번째 행만 필터링
ORDER BY 
    DATETIME ASC;  -- 보호 시작일 오름차순 정렬