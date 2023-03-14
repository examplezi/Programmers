-- 코드를 입력하세요
SELECT pro.product_code, (pro.price *sum(sale.sales_amount)) as sales
from product as pro
join offline_sale as sale on pro.product_id = sale.product_id
group by pro.product_id
#having
order by sales desc, pro.product_code 