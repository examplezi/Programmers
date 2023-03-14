-- 코드를 입력하세요
# SELECT TITLE, 
#     USED_GOODS_BOARD.BOARD_ID, 
#     REPLY_ID, 
#    USED_GOODS_REPLY.WRITER_ID, 
#     USED_GOODS_REPLY.CONTENTS, DATE_FORMAT(USED_GOODS_REPLY.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
# from USED_GOODS_REPLY,USED_GOODS_BOARD
# where MONTH(USED_GOODS_BOARD.CREATED_DATE) ='10'
# order by USED_GOODS_REPLY.CREATED_DATE ,title


SELECT B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS, DATE_FORMAT(R.CREATED_DATE,'%Y-%m-%d')
FROM USED_GOODS_BOARD as B, USED_GOODS_REPLY as R
WHERE DATE_FORMAT(B.CREATED_DATE,'%Y-%m') = '2022-10'
    AND B.BOARD_ID = R.BOARD_ID
ORDER BY R.CREATED_DATE, B.TITLE;