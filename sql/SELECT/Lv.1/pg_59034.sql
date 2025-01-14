-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/59034?language=oracle
-- 간단한 문제 설명 : 
--   동물 보호소에 들어온 모든 동물의 정보를 ANIMAL_ID순으로 조회하는 문제입니다.
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
--   1. SELECT * 로 모든 컬럼 선택
--   2. ORDER BY ANIMAL_ID로 아이디 기준 오름차순 정렬
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N) - ORDER BY로 인한 정렬
--   - 공간복잡도 : O(N) - 전체 데이터 저장

SELECT *  -- 모든 컬럼 선택
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;  -- 동물 아이디 기준 오름차순 정렬