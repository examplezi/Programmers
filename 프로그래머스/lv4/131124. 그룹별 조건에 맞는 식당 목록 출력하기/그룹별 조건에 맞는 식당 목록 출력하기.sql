-- 코드를 입력하세요
# SELECT profile.MEMBER_NAME, REVIEW_TEXT, date_format(review_date,'%Y-%m-%d') as REVIEW_DATE
# from member_profile profile
# join rest_review review on profile.member_id = review.member_id
# where count(review_date)
# group by profile.member_id
# order by REVIEW_DATE ,REVIEW_TEXT


SELECT member_name,review_text,date_format(review_date, '%Y-%m-%d') review_date
FROM member_profile A 
join rest_review B USING (member_id)
WHERE member_id =(SELECT member_id FROM rest_review GROUP BY member_id ORDER BY count(member_id) DESC LIMIT 1)
ORDER BY review_date, review_text