-- 코드를 입력하세요
SET @startnum =0
SET @endnum =24;

WITH gen AS (
    SELECT @startnum AS num
    UNION ALL
    SELECT num+1 FROM gen WHERE num+1<=@endnum
);

SELECT * FROM gen;
-- SELECT hour(DATETIME) as "HOUR", COUNT(HOUR) as "COUNT"
--     FROM ANIMAL_OUTS
--     GROUP BY HOUR
--     HAVING HOUR <= 23
--     ORDER BY HOUR;