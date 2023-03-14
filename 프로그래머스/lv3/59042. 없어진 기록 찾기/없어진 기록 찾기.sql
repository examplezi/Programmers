-- 코드를 입력하세요 animal_id
# SELECT ins.animal_id, ins.name
# from animal_ins as ins
# join animal_outs as outs on ins.animal_id = outs.animal_id 


SELECT
    outs.animal_id, outs.name
FROM animal_outs AS outs
	LEFT JOIN animal_ins AS ins
	ON outs.animal_id = ins.animal_id
WHERE
    ins.animal_id IS NULL;