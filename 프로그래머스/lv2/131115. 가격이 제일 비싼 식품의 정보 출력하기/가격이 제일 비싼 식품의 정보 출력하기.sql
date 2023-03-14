-- 코드를 입력하세요
# SELECT product_id, product_name, product_cd, category, MAX(price) as PRICE
# from food_product 


 SELECT * 
 FROM FOOD_PRODUCT
 WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT)