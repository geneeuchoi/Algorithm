-- 코드를 입력하세요
SELECT date_format(DATETIME, '%H') HOUR,
count(*)
FROM ANIMAL_OUTS
WHERE date_format(DATETIME, '%H') between '08:00:00' and '19:59:00'
GROUP BY HOUR
ORDER BY HOUR