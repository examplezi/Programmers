SELECT A.REST_ID, B.REST_NAME, B.FOOD_TYPE, B.FAVORITES, B.ADDRESS, ROUND(AVG(A.REVIEW_SCORE),2) AS SCORE
FROM REST_REVIEW A
JOIN REST_INFO B ON A.REST_ID = B.REST_ID
GROUP BY A.REST_ID
HAVING B.ADDRESS LIKE '서울%'
ORDER BY SCORE DESC, B.FAVORITES DESC


# select a.rest_id, a.rest_name, a.food_type, a.favorites,a.address, ROUND(AVG(b.REVIEW_SCORE),2) AS SCORE
# from rest_info as a
# join rest_review as b on a.rest_id = b.rest_id
# group by a.rest_id
# having a.address like '서울%'
# order by SCORE desc, a.favorites desc