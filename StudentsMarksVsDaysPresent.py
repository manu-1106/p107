import pandas as pd
import plotly.express
df= pd.read_csv('StudentMarksVsDaysPresent.csv')
print(df.groupby('Marks In Percentage')['Days Present'].mean())
fig=px.scatter(df,x='Marks In Percentage',y='Days Present',size='Marks In Percentage',color='Days Present')