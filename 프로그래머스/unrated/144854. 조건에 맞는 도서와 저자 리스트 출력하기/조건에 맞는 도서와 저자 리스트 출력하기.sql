-- 코드를 입력하세요
SELECT book.book_id, author.author_name, date_format(book.published_date,'%Y-%m-%d')
from book
join author on book.author_id = author.author_id
where category = '경제'
order by published_date