# Write your MySQL query statement below
select query_name, ROUND(SUM(rating/position) / Count(query_name),2) as quality , ROUND(SUM(IF(rating < 3, 1, 0)) *100 / COUNT(query_name), 2) as poor_query_percentage
from Queries
GROUP BY query_name