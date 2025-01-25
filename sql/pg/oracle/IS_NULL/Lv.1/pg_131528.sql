-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/131528?language=oracle
-- 간단한 문제 설명 :
--   USER_INFO 테이블에서 나이(AGE)가 NULL인 회원 수를 'USERS'라는 컬럼명으로 조회
--
-- 테이블 스키마 :
--   - 테이블명 : USER_INFO
--   - 주요 컬럼 :
--       USER_ID INTEGER  NOT NULL -- 회원 ID
--       GENDER  TINYINT(1)       -- 성별 (0: 남자, 1: 여자, NULL 가능)
--       AGE     INTEGER          -- 나이 (NULL 가능)
--       JOINED  DATE    NOT NULL -- 가입일
--
-- 해결 방법 설명 :
--   1) WHERE 절에 AGE IS NULL 조건을 사용하여 나이 정보가 없는 회원만 필터링
--   2) COUNT(*) 함수를 사용해 해당 회원의 수를 구함
--   3) 결과 컬럼명을 USERS로 지정
--
-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT COUNT(*) : 해당 조건을 만족하는 행의 개수를 반환
--   - IS NULL : 컬럼값이 NULL인지 판별
--   - AS : 별칭(alias) 지정
--
-- 쿼리 최적화 방법 :
--   - AGE 컬럼에 인덱스를 두면 WHERE AGE IS NULL 조건의 수행 속도가 빨라질 수 있음 
--     (하지만 NULL 인덱싱 지원은 DB별로 차이가 있음)
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N) (테이블 전체 스캔)
--   - 공간복잡도 : O(1) (단일 결과값)

SELECT 
    COUNT(*) AS USERS
FROM 
    USER_INFO
WHERE 
    AGE IS NULL;