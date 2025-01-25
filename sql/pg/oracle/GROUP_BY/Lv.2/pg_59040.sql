-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/59040?language=oracle
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

SELECT ANIMAL_TYPE, COUNT(*) AS count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE ASC;