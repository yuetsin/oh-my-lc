SELECT id
	, CASE 
		WHEN id % 2 = 0 THEN lag
		ELSE 
			CASE 
				WHEN lead IS NULL THEN student
				ELSE lead
			END
	END AS student
FROM (
	SELECT id, lead(student) OVER (ORDER BY id) AS lead, student
		, lag(student) OVER (ORDER BY id) AS lag
	FROM seat
) sub