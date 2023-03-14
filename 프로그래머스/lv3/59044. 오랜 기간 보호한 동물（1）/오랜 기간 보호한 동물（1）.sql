-- 코드를 입력하세요
SELECT ins.name, ins.datetime
from animal_ins as ins

left join animal_outs as outs on outs.animal_id = ins.animal_id
where outs.datetime is null
order by ins.datetime
limit 3