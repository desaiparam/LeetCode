# Write your MySQL query statement below
select LEFT(trans_date,7) as month, country,COUNT(id) as trans_count,SUM(state ='approved') as approved_count, sum(amount) as trans_total_amount, SUM((state ='approved') * amount) as approved_total_amount
from Transactions
GROUP BY month,country
