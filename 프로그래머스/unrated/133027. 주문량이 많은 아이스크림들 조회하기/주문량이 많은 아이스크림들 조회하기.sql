-- 코드를 입력하세요
# SELECT half.flavor  
# from first_half half
# join july on half.shipment_id = july.shipment_id
# where sum(half.total_order, july.total_order)
# group by half.shipment_id
# order by half.flavor  
# limit 3

SELECT half.flavor  
from first_half half
join july on half.flavor = july.flavor
#where sum(half.total_order, july.total_order)
group by half.flavor  
order by sum(half.total_order) + sum(july.total_order) desc
limit 3