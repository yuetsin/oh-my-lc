# Write your MySQL query statement below

SELECT Request_at AS "Day"
	, Round(COUNT(CASE Status
		WHEN 'completed' THEN NULL
		ELSE 1
	END) / COUNT(*), 2) AS "Cancellation Rate"
FROM Trips
WHERE Client_Id IN (
		SELECT Users_Id
		FROM Users
		WHERE Role = 'client'
			AND Banned = 'No'
	)
	AND Driver_Id IN (
		SELECT Users_Id
		FROM Users
		WHERE Role = 'driver'
			AND Banned = 'No'
	)
GROUP BY Request_at
HAVING Day BETWEEN '2013-10-01' AND '2013-10-03'