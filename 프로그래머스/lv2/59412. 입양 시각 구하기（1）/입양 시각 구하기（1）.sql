-- 코드를 입력하세요
# SELECT date_format(datetime,'%H:%i') as hour, count 
# from animal_outs 
# where truncate(hour,)
# group by hour

# order by hour 
SELECT HOUR(DATETIME) AS HOUR, COUNT(DATETIME) AS COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) <= 19
GROUP BY HOUR 
ORDER BY HOUR;