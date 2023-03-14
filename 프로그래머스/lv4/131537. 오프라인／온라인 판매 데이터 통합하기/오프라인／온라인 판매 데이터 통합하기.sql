# -- 코드를 입력하세요
# SELECT sales_date, product_id, user_id, sales_amount
# from online_sale, offline_sale 
# where
# order by sales_date, product_id, user_id



SELECT DATE_FORMAT(SALES_DATE, "%Y-%m-%d") AS SALES_DATE,
PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE
WHERE DATE_FORMAT(sales_date,'%Y-%m') = '2022-03'
UNION ALL
SELECT DATE_FORMAT(SALES_DATE, "%Y-%m-%d") AS SALES_DATE,
PRODUCT_ID, 
NULL AS USER_ID
, SALES_AMOUNT
FROM OFFLINE_SALE
WHERE DATE_FORMAT(sales_date,'%Y-%m') = '2022-03'
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID