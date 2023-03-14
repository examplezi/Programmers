-- 코드를 입력하세요
SELECT ins.animal_id, ins.animal_type, ins.name
from animal_ins ins
join animal_outs outs on ins.animal_id = outs.animal_id
#where ins.sex_upon_intake like "Intact%" and outs.sex_upon_outcome in ("Spayed", "Neutered")
where ins.sex_upon_intake like "Intact%" and (outs.SEX_UPON_OUTCOME LIKE 'SPAYED%'
OR outs.SEX_UPON_OUTCOME LIKE 'NEUTERED%')
#group by 
order by ins.animal_id