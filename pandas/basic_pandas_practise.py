import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, 4, 5])
# print(s)

s = pd.Series(
    [10, 20, 30],
    # index=["a","b","c"]
    index=[1, 2, 3],
)
print(s)
print(s[[1, 2, 3]])


data = {"Math": 90, "Science": 85, "English": 88}

marks = pd.Series(data)

print(marks)
print(marks.index, marks.values)


print(pd.Series([1, 2, 3, None, None]).isnull())


data = {
    "Name": ["Yashraj", "Sahdev", "Rudra"],
    "Age": [21, 21, 20],
}
df = pd.DataFrame(data)

print(df)

print(df.shape)
print(df.columns)
print(df.index)
print(df.dtypes)
print("=" * 80)
print(df.iloc[1])


import pandas as pd

data = {
    "EmployeeID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Yash", "Ravi", "Amit", "Neha", "Priya", "Karan", "Sneha", "Arjun"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "Marketing"],
    "Age": [20, 24, 22, 30, 28, None, 26, 29],
    "Salary": [50000, 45000, 60000, 75000, None, 65000, 70000, 55000],
    "Experience": [1, 2, 1, 5, 4, 3, 4, 2],
    "City": [
        "Ahmedabad",
        "Delhi",
        "Mumbai",
        "Pune",
        "Delhi",
        "Ahmedabad",
        "Pune",
        "Bangalore",
    ],
}

df = pd.DataFrame(data)

print(df)
df.drop(1, inplace=True)
print(df)
print(df.describe())
print(df["Experience"].value_counts())
print(df["Salary"].agg(["sum", "mean", "max", "min"]))
df.groupby("Department")
print(df.groupby("Department"))

print(df.groupby("Department")["Salary"].mean())
print(df.groupby("Department")["Salary"].sum())
print(df.groupby("Experience")["Salary"].mean())
print(df.groupby("Department")["Name"].count())

print(df.groupby("Department")["Salary"].agg(["mean", "max", "min", "sum"]))


# =====================================
df = pd.read_csv("pandas/employee.csv")


# Level 1 — Basic Practice


print("=" * 100)
print(df.head(5))
print(df.tail(3))
print(df.columns)
print(df.shape)
print(df.dtypes)
print(df["Name"])
print(df[["Name", "Salary"]])
print(df.loc[3])
print(df.iloc[1])
print(df[df["Department"] == "IT"])
print("=" * 100)


# Level 2 — Filtering Practice

print(df[df["Salary"] > 60000])
print(df[df["Age"] < 25])
print(df[df["City"] == "Delhi"])
print(df[(df["Department"] == "IT") & (df["Salary"] > 55000)])
print(df[(df["Department"] == "HR") | (df["Department"] == "Marketing")])
print(df[df["Name"].str.startswith("A")])
print(df[df["City"].str.contains("a")])

print("=" * 100)

# Level 3 — Sorting Practice

print(df.sort_values("Salary"))
print(df.sort_values("Salary", ascending=False))
print(df.sort_values(["Department", "Salary"]))
print(df.sort_values("Age", ascending=False))


# Level 4 — Missing Values Practice


print(df.isnull())
print(df.isnull().sum())

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df)

df["Salary"] = df["Salary"].fillna(df["Salary"].median())
print(df)

df.dropna()
print(df)

# Level 5 — Column Operations

df["Bonus"] = df["Salary"] * 0.10
df["Tax"] = df["Salary"] * 0.05
df["Salary_Category"] = np.where(df["Salary"] > 60000, "High", "Low")
df["City"] = df["City"].str.upper()
df["Salary"] = df["Salary"] + 5000
print(df)


# Level 6 — Summary Functions

print(df["Salary"].mean())
print(df["Salary"].max())
print(df["Age"].min())
print(df["Name"].count())
print(df["Department"].unique())
print(df.groupby("Department")["Name"].count())
print(df.describe())

# Level 7 — GroupBy Practice

print(df.groupby("Department")["Salary"].mean())
print(df.groupby("Department")["Salary"].max())
print(df.groupby("Department")["Salary"].sum())
print(df.groupby("Department")["Name"].count())
print(df.groupby("Department")["Salary"].agg(["mean", "max", "min"]))
print(df.groupby("Department")["Salary"].mean().sort_values())
print(df.groupby("City")["Salary"].mean())


# Level 8 — Advanced Beginner Practice

print(df.sort_values("Salary",ascending=False).head(1))
print(df[df["Experience"] > 3])
