WITH cte AS (
		SELECT id, visit_date, people, row_number() OVER (ORDER BY id) AS rn
		FROM stadium
		WHERE people >= 100
	), 
	cte2 AS (
		SELECT id, visit_date, people, id - rn AS diff
		FROM cte
	)
SELECT id, visit_date, people
FROM cte2
WHERE diff IN (
	SELECT diff
	FROM cte2
	GROUP BY diff
	HAVING COUNT(diff) >= 3
)