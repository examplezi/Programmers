-- 코드를 입력하세요
# SELECT count(name) as count 
# from animal_ins
# group by name



select count (distinct name)
from animal_ins 
where name is not null