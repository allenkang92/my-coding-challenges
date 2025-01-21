-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/59411
-- 간단한 문제 설명 : 
-- 테이블 스키마 :
--   - 테이블명 : 
--   - 컬럼명 및 타입 : 
-- 해결 방법 설명 :
--   1. 쿼리 작성 단계
--   2. 사용한 SQL 문법 및 함수 설명
--   3. 쿼리 최적화 방법 (인덱스 사용, 조인 방식 등)
-- 시간/공간 복잡도 :
--   - 시간복잡도 : 
--   - 공간복잡도 : 



SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A
INNER JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
ORDER BY (B.DATETIME - A.DATETIME + 1) DESC
FETCH FIRST 2 ROWS ONLY 
;