# Write your MySQL query statement below

SELECT s2.id AS id, s1.student AS student
FROM seat s1, seat s2
WHERE ((s1.id - s2.id = 1
		AND s1.id % 2 = 0)
	OR (s2.id - s1.id = 1
		AND s1.id % 2 = 1)
	OR ((s2.id = (
			SELECT MAX(id)
			FROM seat
		)
		AND s1.id = (
			SELECT MAX(id)
			FROM seat
		)
		AND s1.id % 2 = 1)))