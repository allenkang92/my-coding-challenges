-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/77487
-- 간단한 문제 설명 : 
--   - PLACES 테이블을 활용하여 두 개 이상 공간을 등록한 "헤비 유저"가 소유한 장소 정보를 조회
--   - 조회 항목: ID, NAME, HOST_ID
--   - 결과는 ID를 기준으로 오름차순 정렬

-- 테이블 스키마 :
--   - 테이블명 : 
--     - PLACES
--       - ID         INT      NOT NULL  -- 공간의 고유 ID
--       - NAME       VARCHAR  NOT NULL  -- 공간의 이름
--       - HOST_ID    INT      NOT NULL  -- 공간을 소유한 유저의 ID

-- 해결 방법 설명 :
--   1. PLACES 테이블에서 HOST_ID별로 공간의 개수를 집계하여 두 개 이상 등록한 "헤비 유저"를 식별
--   2. 서브쿼리를 사용하여 헤비 유저의 HOST_ID를 추출
--   3. 메인 쿼리에서 PLACES 테이블을 대상으로, 추출된 HOST_ID를 가진 모든 장소를 조회
--   4. 결과를 ID 기준으로 오름차순 정렬

-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT : 특정 컬럼을 선택하여 조회
--   - WHERE 절 : 조건에 맞는 레코드를 필터링
--   - 서브쿼리 : 두 개 이상의 공간을 등록한 호스트를 식별하기 위해 사용
--   - GROUP BY : HOST_ID별로 그룹화하여 COUNT(*) 수행
--   - HAVING : 그룹화된 결과 중 등록된 공간 수가 2개 이상인 경우만 선택
--   - IN 절 : 서브쿼리 결과와 일치하는 HOST_ID를 가진 레코드 선택
--   - ORDER BY : ID를 기준으로 결과를 오름차순 정렬

-- 쿼리 최적화 방법 :
--   - PLACES 테이블의 HOST_ID 컬럼에 인덱스를 생성하여 그룹화 및 검색 성능 향상
--     예시:
--       CREATE INDEX idx_places_host_id ON PLACES(HOST_ID);
--   - 필요한 컬럼만 SELECT 절에 포함시켜 불필요한 데이터 스캔 최소화

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N), PLACES 테이블 전체를 스캔하여 HOST_ID별로 그룹화
--   - 공간복잡도 : O(K), K는 "헤비 유저"의 수

SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE 
    HOST_ID IN (
        SELECT HOST_ID 
        FROM PLACES 
        GROUP BY HOST_ID 
        HAVING COUNT(*) > 1
    )
ORDER BY ID ASC;