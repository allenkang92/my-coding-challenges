-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/59415?language=oracle
-- 간단한 문제 설명 : 
--   동물 보호소에 가장 최근에 들어온 동물의 입소 시간을 조회합니다.
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
--   1. MAX 함수를 사용하여 가장 최근 날짜 조회
--   2. 결과 컬럼명을 '시간'으로 별칭 지정
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N) - 전체 데이터 스캔
--   - 공간복잡도 : O(1) - 단일 결과값만 저장



-- 방법 1: MAX 함수 사용
-- 장점: 간단하고 직관적
-- 단점: 전체 테이블 스캔 필요
SELECT 
    MAX(DATETIME) AS 시간
FROM 
    ANIMAL_INS;

-- 방법 2: ORDER BY + FETCH FIRST ROW ONLY 사용
-- 장점: 인덱스가 있는 경우 더 효율적일 수 있음
-- 단점: Oracle 12c 이상 버전 필요
SELECT 
    DATETIME AS 시간
FROM 
    ANIMAL_INS
ORDER BY 
    DATETIME DESC
FETCH FIRST ROW ONLY;