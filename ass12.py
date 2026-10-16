
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    "Age": [25, 40, np.nan, 35, 50, 28],
    "MonthlyCharges": [500, 800, 600, np.nan, 900, 450],
    "Tenure": [2, 24, 12, 36, np.nan, 5],
    "Churn": ["Yes", "No", "Yes", "No", "No", "Yes"]
}

pd.DataFrame(data).to_csv("customer_churn.csv", index=False)

# Read CSV file
df = pd.read_csv("customer_churn.csv")

print("Original Data:")
print(df)

# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["MonthlyCharges"] = df["MonthlyCharges"].fillna(
    df["MonthlyCharges"].mean()
)
df["Tenure"] = df["Tenure"].fillna(df["Tenure"].median())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Count churned customers
print("\nChurn Count:")
print(df["Churn"].value_counts())

# Visualize churn
df["Churn"].value_counts().plot(kind="bar", color="skyblue")
plt.title("Customer Churn")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# Read CSV file
df = pd.read_csv("customer_churn.csv")

print("Original Data:")
print(df)

# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["MonthlyCharges"] = df["MonthlyCharges"].fillna(
    df["MonthlyCharges"].mean()
)
df["Tenure"] = df["Tenure"].fillna(df["Tenure"].median())

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Count churned customers
print("\nChurn Count:")
print(df["Churn"].value_counts())

# Visualize churn
df["Churn"].value_counts().plot(kind="bar")
plt.title("Customer Churn")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()

