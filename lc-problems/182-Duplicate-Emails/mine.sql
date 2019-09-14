SELECT Email
FROM (
	SELECT Email, COUNT(*) AS Times
	FROM Person
	GROUP BY Email
) Count
WHERE Times > 1