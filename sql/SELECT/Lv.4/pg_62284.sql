-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/62284
-- 간단한 문제 설명 : 
--   - 우유와 요거트를 동시에 구매한 장바구니 ID 조회
--   - 장바구니 ID 오름차순 정렬 필요

-- 테이블 스키마 :
--   - 테이블명 : CART_PRODUCTS
--   - 컬럼명 및 타입 : 
--     - ID INT -- 테이블 ID
--     - CART_ID INT -- 장바구니 ID
--     - NAME VARCHAR -- 상품명
--     - PRICE INT -- 가격

-- 해결 방법 설명 :
--   1. 쿼리 작성 단계
--     - WHERE: 우유와 요거트만 필터링
--     - GROUP BY: 장바구니별 그룹화
--     - HAVING: 두 제품 모두 있는지 확인
--     - ORDER BY: ID 정렬
--   2. 사용한 SQL 문법 및 함수 설명
--     - IN: 여러 값 중 일치하는 것 찾기
--     - COUNT(DISTINCT): 고유한 값의 개수 계산
--     - GROUP BY: 데이터 그룹화
--     - HAVING: 그룹 조건 지정
--   3. 쿼리 최적화 방법
--     - NAME 컬럼에 인덱스 생성 권장
--     - CART_ID에 인덱스 필요

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N), N은 장바구니 상품 수
--   - 공간복잡도 : O(M), M은 장바구니 수

SELECT CART_ID
FROM CART_PRODUCTS 
WHERE NAME IN ('Milk', 'Yogurt')
GROUP BY CART_ID
HAVING COUNT(DISTINCT NAME) = 2
ORDER BY CART_ID ASC;