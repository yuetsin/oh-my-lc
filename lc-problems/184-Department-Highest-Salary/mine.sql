SELECT Department.Name AS `Department`, Outter.Name AS `Employee`, Salary
FROM Employee Outter, Department
WHERE Outter.DepartmentId = Department.Id
	AND Salary >= ALL (
		SELECT Salary
		FROM Employee Iner
		WHERE Iner.DepartmentId = Outter.DepartmentId
	)