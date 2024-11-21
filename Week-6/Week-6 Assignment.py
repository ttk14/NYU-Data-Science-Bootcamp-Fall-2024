import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import warnings
warnings.filterwarnings('ignore')
pd.set_option("display.max_columns", 101)


# Dataset is already loaded below
data = pd.read_csv("employee.csv")

# drop id, timestamp and country columns
data = data.drop(columns=['id', 'timestamp','country'])

# replace NANs in hours_per_week with median value of the column
data.loc[data['hours_per_week'].isna(), 'hours_per_week'] = data['hours_per_week'].median()
data.loc[data['telecommute_days_per_week'].isna(), 'telecommute_days_per_week'] = data['telecommute_days_per_week'].median()

# Handling null values in categorical columns
data = data.dropna()

# Encoding binary variables
binary_cols = ['is_manager', 'certifications']
for c in binary_cols:
    data_train[c] = data_train[c].replace(to_replace=['Yes'], value=1)
    data_train[c] = data_train[c].replace(to_replace=['No'], value=0)

cat_cols = ['employment_status', 'job_title', 'education', 'is_education_computer_related']
final_data = pd.get_dummies(data, columns=cat_cols, drop_first=True, dtype=int)

y = final_data['salary']
X = final_data.drop(columns=['salary'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print("Training Set Dimensions:", X_train.shape)
print("Validation Set Dimensions:", X_test.shape)

# Apply StandardScaler
num_cols = ['job_years', 'hours_per_week', 'telecommute_days_per_week']
scaler = StandardScaler()
scaler.fit(X_train[num_cols])
X_train[num_cols] = scaler.transform(X_train[num_cols])
X_test[num_cols] = scaler.transform(X_test[num_cols])

# Linear Regression Model
reg = LinearRegression()
reg.fit(X_train, y_train)

# Make predictions on the preprocessed test data
y_pred = reg.predict(X_test)

# Calculate Mean Squared Error
mse = mean_squared_error(y_pred, y_test) / np.mean(y_test)
print("Mean Squared Error after preprocessing:", mse)