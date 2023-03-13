-- 코드를 입력하세요
-- joined year() =2021 and age >=20 and age <=29 몇명? count? 
SELECT COUNT (USER_ID) AS USERS
FROM USER_INFO
WHERE YEAR(JOINED) = 2021 and AGE >= 20 and AGE <=29
