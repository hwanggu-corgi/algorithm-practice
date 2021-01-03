-- 코드를 입력하세요
WITH temp AS
(
   SELECT 1 AS HOUR
   UNION ALL
   SELECT DATETIME FROM ANIMAL_OUTS
   WHERE hour(DATETIME) < 24
) -- return table with id from 0 to 24

SELECT * FROM temp;
-- SELECT hour(DATETIME) as "HOUR", COUNT(HOUR) as "COUNT"
--     FROM ANIMAL_OUTS
--     GROUP BY HOUR
--     HAVING HOUR <= 23
--     ORDER BY HOUR;