import pandas as pd

employees = pd.DataFrame(
    {
        "EmpID": [101, 102, 103, 104, 105, 106],
        "Name": ["Yash", "Ravi", "Amit", "Neha", "Priya", "Karan"],
        "DeptID": [1, 2, 1, 3, 4, 2],
        "Salary": [50000, 60000, 55000, 70000, 65000, 52000],
        "City": ["Ahmedabad", "Delhi", "Mumbai", "Pune", "Delhi", "Ahmedabad"],
    }
)

# print(employees)


departments = pd.DataFrame(
    {
        "DeptID": [1, 2, 3, 5],
        "Department": ["IT", "HR", "Finance", "Marketing"],
        "Manager": ["Rajesh", "Anita", "Suresh", "Meera"],
    }
)

# print(departments)


print(pd.merge(employees, departments, on="DeptID", how="inner"))


print(pd.merge(employees, departments, on="DeptID", how="left"))

print(pd.merge(employees, departments, on="DeptID", how="right"))
print(pd.merge(employees, departments, on="DeptID", how="outer"))


print(
    pd.merge(employees, departments, on="DeptID", how="inner")[["Name", "Department"]]
)
print(
    pd.merge(employees, departments, on="DeptID", how="inner")
    .groupby("Department")["Salary"]
    .max()
)

merged = pd.merge(employees, departments, on="DeptID", how="inner")

# print(merged)
import numpy as np

print(merged[merged["Department"] == "IT"])
print(merged.groupby("Department")["Salary"].mean())

print(merged[merged["Manager"] == "Anita"])
print(merged.sort_values("Salary", ascending=False))

print(merged[merged["City"] == "Delhi"])
print(merged.groupby("Department")["Name"].count())

merged["Salary_Category"] = np.where(merged["Salary"] > 60000, "High", "Low")
print(merged)

print(
    pd.merge(employees, departments, on="DeptID", how="right")[
        lambda df: df["Name"].isnull()
    ]
)
