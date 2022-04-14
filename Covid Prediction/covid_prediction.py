# -*- coding: utf-8 -*-
"""Covid Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T0l3F-AYm5Jzt6D7rfFF7dHv8h7gnLBd
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import seaborn as sns
import numpy as np
from google.colab import files
import io

import plotly
import plotly.express as px
import plotly.graph_objects as go
from sklearn.metrics import average_precision_score
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
import datetime as dt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import mean_squared_error
from matplotlib import style
style.use('ggplot')
# %matplotlib inline
plt.rcParams['figure.figsize']=20,10

uploaded = files.upload()

df = pd.read_csv(io.BytesIO(uploaded['covid.csv']))

df.describe()

df.shape

df.head()

df.isnull().sum()

df.plot(kind='bar',x='new_deaths',y = 'total_deaths', color='red')
plt.xlabel('total deaths')
plt.ylabel('new deaths')
plt.title('Relation between new and total deaths')
plt.show()

fig = px.scatter(df, x="new_cases", y="new_deaths", color="total_cases", hover_data=['date'], title='situation of new cases and deaths')
fig.show()

x = df.iloc[:,1].values
y = df.iloc[:,4].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(x,y, test_size=0.25, random_state = 0)

from sklearn.linear_model import LinearRegression

x = x.reshape(-1,1)

classifier = LinearRegression()
classifier.fit(np.array(X_train).reshape(-1,1),np.array(Y_train).reshape(-1,1))

y_pred=classifier.predict(np.array(X_test).reshape(-1,1))

mean_squared_error(X_test,y_pred)

from sklearn.metrics import accuracy_score
accuracy = classifier.score(x,y)
print(f'Accuracy:{round(accuracy*100,3)} %')

