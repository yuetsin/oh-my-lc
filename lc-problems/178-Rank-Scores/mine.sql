# Write your MySQL query statement below

# DENSE RANK

SELECT Score, IFNULL((
		SELECT COUNT(DISTINCT Score)
		FROM Scores
		WHERE Score > s.Score
	) + 1, 1) AS Rank
FROM Scores s
ORDER BY Score DESC;