CREATE FUNCTION getNthHighestSalary (
	N INT
)
RETURNS INT
BEGIN
	DECLARE var int;
	SET var = N - 1;
	RETURN 
		SELECT (
				SELECT DISTINCT Salary
				FROM Employee
				ORDER BY Salary DESC
				LIMIT var, 1
			);
END