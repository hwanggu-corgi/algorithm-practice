-- Reference: https://stackoverflow.com/questions/4740612/query-to-convert-from-datetime-to-date-mysql
-- SELECT DATE_FORMAT('2004-01-20' ,'%Y-%m-01');

-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, "%Y-%m-%d") AS "날짜"
    FROM ANIMAL_INS;