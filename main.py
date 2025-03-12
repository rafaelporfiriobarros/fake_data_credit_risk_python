import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker
fake = Faker()

# Set seed for reproducibility
np.random.seed(42)

# Number of samples
num_samples = 5000

# Generate synthetic data
data = {
    "Customer_ID": [fake.uuid4() for _ in range(num_samples)],
    "Age": np.random.randint(18, 75, num_samples),
    "Gender": np.random.choice(["Male", "Female"], num_samples),
    "Annual_Income": np.random.randint(20000, 150000, num_samples),
    "Loan_Amount": np.random.randint(1000, 50000, num_samples),
    "Credit_Score": np.random.randint(300, 850, num_samples),
    "Late_Payments": np.random.randint(0, 10, num_samples),
    "Loan_Term": np.random.choice([12, 24, 36, 48, 60], num_samples),
    "Interest_Rate": np.round(np.random.uniform(3.5, 25, num_samples), 2),
    "Loan_Type": np.random.choice(["Personal", "Mortgage", "Auto", "Education"], num_samples),
}

# Define the target variable (Default: 1 = Default, 0 = No Default)
data["Default"] = np.where(
    (data["Credit_Score"] < 600) & (data["Late_Payments"] > 3) & (data["Annual_Income"] < 40000),
    1,  # Default
    0   # No Default
)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV (Optional)
df.to_csv("synthetic_credit_risk.csv", index=False)

# Display first rows
df.head()
