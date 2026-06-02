import pandas as pd
import numpy as np

# ==================================================
# Load Dataset
# ==================================================

df = pd.read_csv("pandas/train.csv")

# ==================================================
# Level 1: Dataset Exploration
# ==================================================

# 1. Display first 10 rows.
print(df.head(10))

# 2. Display last 15 rows.
print(df.tail(15))

# 3. Find shape of dataset.
print(df.shape)

# 4. List all columns.
print(df.columns)

# 5. Check data types of all columns.
print(df.dtypes)

# 6. Get summary statistics.
print(df.describe())

# 7. Find missing values in each column.
print(df.isnull().sum())

# 8. Count total passengers.
print(df["PassengerId"].count())

# 9. Find number of unique ticket numbers.
print(df["Ticket"].nunique())

# 10. Find number of unique cabins.
print(df["Cabin"].nunique())


# ==================================================
# Level 2: Basic Filtering
# ==================================================

# 1. Find all male passengers.
print(df[df["Sex"] == "male"])

# 2. Find all female passengers.
print(df[df["Sex"] == "female"])

# 3. Find passengers older than 50.
print(df[df["Age"] > 50])

# 4. Find passengers younger than 10.
print(df[df["Age"] < 10])

# 5. Find passengers travelling in First Class.
print(df[df["Pclass"] == 1])

# 6. Find passengers travelling in Third Class.
print(df[df["Pclass"] == 3])

# 7. Find passengers whose fare is greater than 100.
print(df[df["Fare"] > 100])

# 8. Find passengers embarked from Southampton (S).
print(df[df["Embarked"] == "S"])

# 9. Find passengers embarked from Cherbourg (C).
print(df[df["Embarked"] == "C"])

# 10. Find passengers with cabin information available.
print(df[df["Cabin"].notna()])


# ==================================================
# Level 3: Sorting
# ==================================================

# 1. Sort passengers by Age ascending.
print(df.sort_values("Age"))

# 2. Sort passengers by Age descending.
print(df.sort_values("Age", ascending=False))

# 3. Sort passengers by Fare descending.
print(df.sort_values("Fare", ascending=False))

# 4. Find top 10 highest fare passengers.
print(df.sort_values("Fare", ascending=False).head(10))

# 5. Find youngest passenger.
print(df.sort_values("Age").head(1))

# 6. Find oldest passenger.
print(df.sort_values("Age", ascending=False).head(1))


# ==================================================
# Level 4: Value Counts
# ==================================================

# 1. Count males and females.
print(df["Sex"].value_counts())

# 2. Count passengers by class.
print(df["Pclass"].value_counts())

# 3. Count passengers by embarkation port.
print(df["Embarked"].value_counts())

# 4. Count passengers by survival status.
print(df["Survived"].value_counts())

# 5. Find most common age.
print(df["Age"].mode()[0])

# 6. Find most common fare.
print(df["Fare"].mode()[0])


# ==================================================
# Level 5: GroupBy
# ==================================================

# 1. Average age by gender.
print(df.groupby("Sex")["Age"].mean())

# 2. Average fare by class.
print(df.groupby("Pclass")["Fare"].mean())

# 3. Average fare by embarkation port.
print(df.groupby("Embarked")["Fare"].mean())

# 4. Average age by passenger class.
print(df.groupby("Pclass")["Age"].mean())

# 5. Number of passengers in each class.
print(df.groupby("Pclass")["PassengerId"].count())

# 6. Count passengers by gender and class.
print(df.groupby(["Sex", "Pclass"])["PassengerId"].count())

# 7. Maximum fare paid in each class.
print(df.groupby("Pclass")["Fare"].max())

# 8. Minimum fare paid in each class.
print(df.groupby("Pclass")["Fare"].min())


# ==================================================
# Level 6: Survival Analysis
# ==================================================

# 1. Overall survival rate.
print(df["Survived"].mean() * 100)

# 2. Survival rate by gender.
print(df.groupby("Sex")["Survived"].mean() * 100)

# 3. Survival rate by passenger class.
print(df.groupby("Pclass")["Survived"].mean() * 100)

# 4. Survival rate by embarkation port.
print(df.groupby("Embarked")["Survived"].mean() * 100)

# 5. Average age of survivors.
print(df.groupby("Survived")["Age"].mean()[1])

# 6. Average age of non-survivors.
print(df.groupby("Survived")["Age"].mean()[0])

# 7. Which gender had highest survival rate?
print(df.groupby("Sex")["Survived"].mean().idxmax())

# 8. Which class had highest survival rate?
print(df.groupby("Pclass")["Survived"].mean().idxmax())

# 9. Did children survive more than adults?
df["AgeGroup"] = np.where(df["Age"] < 18, "Child", "Adult")
print(df.groupby("AgeGroup")["Survived"].mean() * 100)

# 10. Did passengers paying higher fares survive more?
print(df.groupby("Survived")["Fare"].mean())


# ==================================================
# Level 7: Feature Engineering
# ==================================================

# 1. Create FareCategory using pd.cut()

df["FareCategory"] = pd.cut(
    df["Fare"],
    bins=[0, 50, 100, 200, 600],
    labels=["Low", "Medium", "High", "Luxury"]
)

# 2. Create AgeGroup using pd.cut()

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 18, 50, 100],
    labels=["Child", "Adult", "Senior"]
)

# 3. Create FamilySize column.
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# 4. Create IsAlone column.
df["IsAlone"] = df["FamilySize"] == 1

# 5. Extract Title from Name.
df["Title"] = df["Name"].str.extract(r',\s*([^\.]+)\.')


# ==================================================
# Level 8: Multi-Level Analysis
# ==================================================

# 1. Average fare by Gender and Class.
print(df.groupby(["Sex", "Pclass"])["Fare"].mean())

# 2. Survival rate by Gender and Class.
print(df.groupby(["Sex", "Pclass"])["Survived"].mean() * 100)

# 3. Top 10 passengers who paid highest fare.
print(df.sort_values("Fare", ascending=False).head(10))

# 4. Passenger class contributing highest revenue.
print(df.groupby("Pclass")["Fare"].sum().idxmax())


# ==================================================
# Level 9: Advanced GroupBy
# ==================================================

# 1. Find passengers whose age is above average age of their class.

df["AverageAgeByClass"] = (
    df.groupby("Pclass")["Age"]
      .transform("mean")
)

print(df[df["Age"] > df["AverageAgeByClass"]])

# 2. Find oldest passenger in every class.

oldest_idx = (
    df.groupby("Pclass")["Age"]
      .idxmax()
)

print(df.loc[oldest_idx])

# 3. Rank passengers by fare within each class.

df["FareRank"] = (
    df.groupby("Pclass")["Fare"]
      .rank(method="dense", ascending=False)
)

print(df[["Name", "Pclass", "Fare", "FareRank"]].head())


# ==================================================
# Level 10: Reporting
# ==================================================

# 1. Create survival report by class.

survival_report = (
    df.groupby("Pclass")
      .agg(
          TotalPassengers=("PassengerId", "count"),
          Survivors=("Survived", "sum"),
          SurvivalRate=("Survived", "mean")
      )
)

survival_report["Deaths"] = (
    survival_report["TotalPassengers"]
    - survival_report["Survivors"]
)

survival_report["SurvivalRate"] *= 100

print(survival_report)

# 2. Create pivot table for survival analysis.

pivot_survival = pd.pivot_table(
    df,
    values="Survived",
    index="Pclass",
    columns="Sex",
    aggfunc="mean"
)

print(pivot_survival)

# 3. Create pivot table for fare analysis.

pivot_fare = pd.pivot_table(
    df,
    values="Fare",
    index="Pclass",
    columns="Sex",
    aggfunc="mean"
)

print(pivot_fare)