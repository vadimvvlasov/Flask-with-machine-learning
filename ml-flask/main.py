# https://medium.com/analytics-vidhya/deploying-a-machine-learning-model-on-web-using-flask-and-python-54b86c44e14a

# Step1. Importing all the necessary Libraries required for building a Linear Regression Model using Scikit Learn
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

# Step2. Reading the data using pandas and defining our variables for training
df = pd.DataFrame({
    "area": [2600, 3000, 3200, 3600, 4000],
    "price": [550000, 565000, 610000, 680000, 725000]
})

print(df)

x = df[['area']]
y = df[['price']]

# Step3. Training our model
reg = linear_model.LinearRegression()
reg.fit(x, y)

# Step4. Calculating the score along with coefficients and doing prediction on a certain value of the area variable.
print(reg.score(x, y))
print(reg.predict([[3300]]))
print(reg.coef_)
print(reg.intercept_)

import joblib

joblib.dump(reg, "linear_reg.pkl")
