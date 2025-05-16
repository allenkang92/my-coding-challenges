-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/157341
-- 간단한 문제 설명 :
--   - CAR_RENTAL_COMPANY_CAR 테이블과 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블 전적을 활용
--   - 10월에 대여를 시작한 (START_DATE) '세단' 자동차들의 CAR_ID를 내림차순 정렬, 중복 없이 출력

-- 테이블 스키마 :
--   - CAR_RENTAL_COMPANY_CAR : 자동차 운영정보(자동차 ID, 종류, 일일 요금, 옵션)
--     - CAR_ID       INTEGER    NOT NULL
--     - CAR_TYPE     VARCHAR(255) NOT NULL
--     - DAILY_FEE    INTEGER    NOT NULL
--     - OPTIONS      VARCHAR(255) NOT NULL
--   - CAR_RENTAL_COMPANY_RENTAL_HISTORY : 자동차 대여 이력(대여 기록 ID, 자동차 ID, 대여 시작일, 종료일)
--     - HISTORY_ID   INTEGER    NOT NULL
--     - CAR_ID       INTEGER    NOT NULL
--     - START_DATE   DATE       NOT NULL
--     - END_DATE     DATE       NOT NULL

-- 해결 방법 설명 :
--   1. CAR_RENTAL_COMPANY_CAR와 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블을 CAR_ID로 조인
--   2. 10월에 대여를 시작한 대여 이력을 필터링(TO_CHAR(START_DATE, 'MM') = '10')
--   3. 자동차 종류가 '세단'으로 등록된 데이터만 조회
--   4. 중복 없이 DISTINCT, 자동차 ID(CAR_ID)를 기준으로 내림차순(ORDER BY DESC)

-- 사용한 SQL 문법 및 함수 설명 :
--   - TO_CHAR(START_DATE, 'MM') = '10': START_DATE의 월을 'MM' 형태의 문자열로 변환 후, '10'과 비교
--   - INNER JOIN ... ON ... : 두 테이블의 공통키(CAR_ID) 기준으로 내부 조인
--   - DISTINCT: 중복 레코드를 제거
--   - ORDER BY CAR_ID DESC: 자동차 ID 내림차순 정렬

-- 쿼리 최적화 방법 (인덱스 사용, 조인 방식 등) :
--   - CAR_ID 컬럼에 인덱스 생성: 두 테이블 간 조인 성능 향상
--   - START_DATE 컬럼에도 인덱스 적용 가능 (월별 조회 빈도가 높을 경우)

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N), 전체 데이터를 스캔 후 조건 필터링 및 정렬
--   - 공간복잡도 : O(N), 결과 집합을 정렬하기 위한 임시 공간

SELECT DISTINCT A.CAR_ID AS CAR_ID
FROM CAR_RENTAL_COMPANY_CAR A
INNER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY B ON A.CAR_ID = B.CAR_ID
WHERE TO_CHAR(B.START_DATE, 'MM') = '10'
  AND A.CAR_TYPE = '세단'
ORDER BY CAR_ID DESC;