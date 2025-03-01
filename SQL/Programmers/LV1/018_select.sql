-- LV1
-- SELECT
-- 과일로 만든 아이스크림 고르기

SELECT
    FH.FLAVOR
FROM
    FIRST_HALF FH
JOIN
    ICECREAM_INFO II
ON FH.FLAVOR = II.FLAVOR
WHERE
    FH.TOTAL_ORDER > 3000
    AND II.INGREDIENT_TYPE = 'fruit_based'
ORDER BY
    TOTAL_ORDER DESC