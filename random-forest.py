import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

import seaborn as sns

# Import dataframe
df = pd.read_csv("E:\\Mozila Firefox\\train_data.csv")
print(df.head())

# Select Independent and Dependent Variables
x= df[["overallqual", "grlivarea", "garagecars", "ageofhouse"]]
y = df["saleprice"]

# Split the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Instantiate the Model
regressor = RandomForestRegressor(n_estimators=20, random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

# Print Metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# Feature Importance
feature_list = list(x.columns)
print(feature_list)

for name, importance in zip(feature_list, regressor.feature_importances_):
    print(name, "=", importance)

# Plot important features

