SELECT ConsecutiveNums
FROM (
	SELECT Num AS ConsecutiveNums, COUNT(*) AS C
	FROM Logs
	GROUP BY Num
	HAVING C >= 3
) T