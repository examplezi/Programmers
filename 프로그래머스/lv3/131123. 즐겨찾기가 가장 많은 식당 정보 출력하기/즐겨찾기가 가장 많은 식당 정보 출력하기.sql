-- 코드를 입력하세요
# SELECT food_type, rest_id, rest_name, max(favorites)
# from rest_info 
# #where
# group by food_type
# having max(favorites) limit 1
# order by food_type desc


# having
# SELECT food_type,rest_id,rest_name,favorites
# from rest_info
# group by food_type
# having (max(favorites))
# order by food_type desc


#where
SELECT food_type,rest_id,rest_name,favorites from rest_info
where favorites in (select max(favorites)  from rest_info
                   group by food_type)
group by food_type
order by food_type desc