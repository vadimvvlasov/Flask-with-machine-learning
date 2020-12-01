# building a simple Linear Regression model in Python

# ----------------- Step1. Importing all the necessary Libraries -----------------
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import joblib

# ----------------- Step2. Reading the data and defining our variables for training -----------------
df = pd.read_csv('homeprices.csv')

x=df[['area']]
y=df[['price']]

# ----------------- Step3. Training our model -----------------
reg = linear_model.LinearRegression()
reg.fit(x,y)

print(f"score = {reg.score(x,y)}")
print(f"predict(area=3300) = {reg.predict([[3300]])}")
print(f"coef = {reg.coef_}, intercept={reg.intercept_}")

# ----------------- Step4. save the above as .pkl file -----------------
joblib.dump(reg,"linear_reg.pkl")