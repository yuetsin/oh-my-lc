/* Write your T-SQL query statement below */

SELECT id, movie, description, rating
FROM cinema
WHERE id % 2 <> 0
	AND description <> 'Boring'
ORDER BY rating DESC