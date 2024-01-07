-- 프로그래머스
-- SQL 고득점 Kit : IS NULL
-- 이름이 없는 동물의 아이디

-- Oracle
-- NVL()
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY ANIMAL_ID ASC;


-- MySQL
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY ANIMAL_ID ASC;