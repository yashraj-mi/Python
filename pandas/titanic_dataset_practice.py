import pandas as pd
df=pd.read_csv("/kaggle/input/datasets/yashrajmi/titanic-dataset/test.csv")


# Level 1: Dataset Exploration


# 1. Display first 10 rows.
# 2. Display last 15 rows.
# 3. Find shape of dataset.
# 4. List all columns.
# 5. Check data types of all columns.
# 6. Get summary statistics.
# 7. Find missing values in each column.
# 8. Count total passengers.
# 9. Find number of unique ticket numbers.
# 10. Find number of unique cabins.


print(df.head(10))
print(df.tail(15))
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.describe())
print(df.isnull())
print(df["PassengerId"].count())
print(df["Ticket"].nunique())
print(df["Cabin"].nunique())


# Level 2: Basic Filtering
# 1. Find all male passengers.
# 2. Find all female passengers.
# 3. Find passengers older than 50.
# 4. Find passengers younger than 10.
# 5. Find passengers travelling in First Class.
# 6. Find passengers travelling in Third Class.
# 7. Find passengers whose fare is greater than 100.
# 8. Find passengers embarked from Southampton (S).
# 9. Find passengers embarked from Cherbourg (C).
# 10. Find passengers with cabin information available.


print(df[df["Sex"]=="male"])
print(df[df["Sex"]=="female"])
print(df.loc[df["Age"]>50])
print(df.loc[df["Age"]<10])
print(df.loc[df["Pclass"]==1])
print(df.loc[df["Pclass"]==3])
print(df[df["Fare"]>100])
print(df.loc[df["Embarked"]=="S"])
print(df.loc[df["Embarked"]=="C"])
print(df.loc[~df["Cabin"].isna()])



# Level 3: Sorting

# 1. Sort passengers by Age ascending.
# 2. Sort passengers by Age descending.
# 3. Sort passengers by Fare descending.
# 4. Find top 10 highest fare passengers.
# 5. Find youngest passenger.
# 6. Find oldest passenger.

print(df.sort_values("Age",ascending=True))
print(df.sort_values("Age",ascending=False))
print(df.sort_values("Fare",ascending=False))
print(df.sort_values("Fare",ascending=False).head(10))
print(df.sort_values("Age").head(1))
print(df.sort_values("Age",ascending=False).head(1))


