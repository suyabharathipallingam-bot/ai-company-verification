import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv("data/companies.csv")

X = df[['Domain_Age','SSL','Complaints']]
y = df['Fraud_Label']

model = RandomForestClassifier()
model.fit(X,y)

pickle.dump(model,open("model/fraud_model.pkl","wb"))

print("Model trained successfully")