-- 코드를 입력하세요
SELECT ingredient_type, sum(total_order) as total_order
from first_half as f
join icecream_info as i on f.flavor = i.flavor
#where f.flavor = i.flavor
group by ingredient_type
order by total_order 


# SELECT ingredient_type AS INGREDIENT_TYPE, SUM(TOTAL_ORDER) AS TOTAL_ORDER
# FROM first_half fh 
#INNER JOIN icecream_info ii
# ON fh.flavor = ii.flavor
# GROUP BY ingredient_type
# ORDER BY TOTAL_ORDER ASC
