# -- 코드를 입력하세요
# SELECT product_id, product_name, product_cd, category, MAX(price) as PRICE
# from food_product 
# group by product_id, product_name, product_cd, category
# having MAX(price)
 # SELECT * 
 # FROM FOOD_PRODUCT
 # WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT)
 
 # select *
 # from food_product
 # where price = (select max(price) from food_product)
 
  select *
 from food_product
 where price = (select max(price) from food_product)