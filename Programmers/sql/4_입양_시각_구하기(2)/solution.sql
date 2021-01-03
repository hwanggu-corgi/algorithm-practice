-- 코드를 입력하세요
SET @start=0;
SET @end=24;

WITH temp(v) AS
(
   SELECT @start AS HOUR, COUNT(hour(DATETIME))
   UNION ALL
   SELECT DATETIME FROM ANIMAL_OUTS
   WHERE v < @end
) -- return table with id from 0 to 24

SELECT * FROM temp;
-- SELECT hour(DATETIME) as "HOUR", COUNT(HOUR) as "COUNT"
--     FROM ANIMAL_OUTS
--     GROUP BY HOUR
--     HAVING HOUR <= 23
--     ORDER BY HOUR;