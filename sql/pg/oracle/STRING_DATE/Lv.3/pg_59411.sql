-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/59411
-- 간단한 문제 설명 : 
--   - ANIMAL_INS 테이블과 ANIMAL_OUTS 테이블을 활용하여, 입양을 간 동물 중 
--     보호 기간이 가장 길었던 동물 2마리의 ID와 이름을 조회
--   - 보호 기간은 (OUT_DATE - IN_DATE + 1)로 계산
--   - 보호 기간이 긴 순으로 정렬 후 상위 2마리만 조회
--
-- 테이블 스키마 :
--   - ANIMAL_INS(ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE)
--   - ANIMAL_OUTS(ANIMAL_ID, ANIMAL_TYPE, DATETIME, NAME, SEX_UPON_OUTCOME)
--   -- 두 테이블은 ANIMAL_ID로 조인
--
-- 해결 방법 설명 :
--   1. ANIMAL_INS와 ANIMAL_OUTS를 INNER JOIN 하여 보호 시작일과 종료일(입양일) 데이터를 함께 조회
--   2. (B.DATETIME - A.DATETIME + 1)로 보호 기간을 계산
--   3. ORDER BY를 사용해 보호 기간을 내림차순 정렬
--   4. FETCH FIRST 2 ROWS ONLY로 상위 2마리만 가져옴
--
-- 사용한 SQL 문법 및 함수 설명 :
--   - DATE 연산: (OUT_DATE - IN_DATE)는 일(day) 단위 차이
--   - ORDER BY ~ DESC: 내림차순 정렬
--   - FETCH FIRST 2 ROWS ONLY: 최상위 2개 결과만 조회
--
-- 쿼리 최적화 방법 :
--   - ANIMAL_ID 컬럼에 인덱스를 생성하여 조인 성능을 높일 수 있음
--   - 필요한 컬럼만 SELECT하여 불필요한 I/O 줄임
--
-- 시간/공간 복잡도 :
--   - 시간복잡도: O(N), 테이블 전체를 스캔한 후 조인 및 정렬
--   - 공간복잡도: O(N), 정렬 과정에서 임시 공간 사용 가능

SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A
INNER JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
ORDER BY (B.DATETIME - A.DATETIME + 1) DESC
FETCH FIRST 2 ROWS ONLY
;