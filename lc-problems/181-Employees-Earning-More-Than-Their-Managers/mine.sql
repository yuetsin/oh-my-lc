# Write your MySQL query statement below

SELECT Name AS Employee
FROM (
	SELECT E.Name, E.Salary AS ESalary, M.Salary AS MSalary
	FROM Employee E, Employee M
	WHERE E.ManagerId = M.Id
) T
WHERE ESalary > MSalary