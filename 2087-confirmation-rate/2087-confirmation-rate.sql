# Write your MySQL query statement below
SELECT s.user_id, ROUND(IFNULL(AVG(action = 'confirmed'),0),2) as confirmation_rate
From Signups as s
LEFT JOIN Confirmations as c
ON s.user_id = c.user_id
GROUP BY s.user_id