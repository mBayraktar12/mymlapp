import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

constant = np.random.randint(0,5,50)

x = np.random.randint(0,10,50)

y = constant + 3 * x

df = pd.DataFrame({'x':x, 'y':y})
print(df.sample(5))

model = LinearRegression()
model.fit(x.reshape(-1,1),df.y)

joblib.dump(model, 'my_model')

j_model = joblib.load('my_model')

print(j_model.predict([[10]]))






