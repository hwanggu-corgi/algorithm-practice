-- Reference: https://stackoverflow.com/questions/4740612/query-to-convert-from-datetime-to-date-mysql
-- SELECT
--     CONVERT(DATE, GETDATE()) date;

-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, DATE(DATETIME) AS "날짜"
    FROM ANIMAL_INS;