-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/59039?language=oracle
-- 간단한 문제 설명 :
--   ANIMAL_INS 테이블에서 NAME이 NULL인 동물의 ID만 조회하고, 결과를 ANIMAL_ID 오름차순으로 정렬.
--
-- 테이블 스키마 :
--   - 테이블명 : ANIMAL_INS
--   - 주요 컬럼 :
--       ANIMAL_ID VARCHAR(N)    NOT NULL  -- 동물 아이디
--       NAME VARCHAR(N)         TRUE      -- 동물 이름 (NULL 가능)
--       ... (기타 컬럼 생략)
--
-- 해결 방법 설명 :
--   1) WHERE 절로 NAME IS NULL 조건을 사용하여 이름이 없는 동물만 필터링.
--   2) ORDER BY ANIMAL_ID ASC로 동물 아이디 기준 오름차순 정렬.
--
-- 사용한 SQL 문법 :
--   - SELECT/FROM/WHERE/ORDER BY 문법 사용.
--   - IS NULL : NULL 여부 확인.
--   - ASC(오름차순 정렬) : 알파벳/숫자 순서로 결과 정렬.
--
-- 쿼리 최적화 관점 :
--   - NAME 컬럼에 인덱스가 있을 경우 WHERE NAME IS NULL이 빠르게 처리될 수 있음.
--   - 전체 테이블 스캔이 일어나도 문제 크기가 크지 않다면 크게 부담되지 않을 수 있음.
--
-- 시간복잡도 :
--   - O(N log N) (정렬로 인해)
-- 공간복잡도 :
--   - O(N) (결과를 저장할 공간)

SELECT 
    ANIMAL_ID
FROM 
    ANIMAL_INS
WHERE 
    NAME IS NULL
ORDER BY 
    ANIMAL_ID ASC;