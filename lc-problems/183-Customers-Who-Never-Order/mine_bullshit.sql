# Write your MySQL query statement below

SELECT Name AS Customers
FROM Customers
WHERE Id NOT IN (
	SELECT Customers.Id
	FROM Customers, Orders
    WHERE Customers.Id = Orders.CustomerId
	GROUP BY Customers.Id
	HAVING COUNT(*) != 0
);