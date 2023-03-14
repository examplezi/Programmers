-- 코드를 입력하세요
SELECT pro.product_id, pro.product_name, sum(pro.price * (orders.amount)) as total_sales
from food_product pro
join food_order orders on pro.product_id = orders.product_id
where date_format(orders.produce_date,'%Y-%m')= '2022-05'
GROUP BY pro.PRODUCT_ID
order by total_sales desc, pro.product_id