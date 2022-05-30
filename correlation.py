import pandas as pd
import plotly.express as px
import numpy as np


#(correlation2)

df=pd.read_csv('D:\MRUDULA KORE\MRUDULA\Python\Projects\Correlation_106\CSV\correlation2.csv')

fig=px.scatter(df,x='Size of TV',y='\tAverage time spent watching TV in a week (hours)')

sizeoftv=df['Size of TV'].tolist()
hours=df['\tAverage time spent watching TV in a week (hours)'].tolist()
correlation=np.corrcoef(x=sizeoftv,y=hours)

print('correlation1= '+str(correlation[0][1]))



#(correlation3)

df=pd.read_csv('D:\MRUDULA KORE\MRUDULA\Python\Projects\Correlation_106\CSV\correlation3.csv')

fig=px.scatter(df,x='Days Present',y='Marks In Percentage')

dayspresent=df['Days Present'].tolist()
marks=df['Marks In Percentage'].tolist()
correlation=np.corrcoef(x=dayspresent,y=marks)

print('correlation2= '+str(correlation[0][1]))


#(correlation4)

df=pd.read_csv('D:\MRUDULA KORE\MRUDULA\Python\Projects\Correlation_106\CSV\correlation4.csv')

fig=px.scatter(df,x='Coffee in ml',y='sleep in hours')

coffee=df['Coffee in ml'].tolist()
sleep=df['sleep in hours'].tolist()
correlation=np.corrcoef(x=coffee,y=sleep)

print('correlation3= '+str(correlation[0][1]))


