
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('student.csv')       # make a data frame

plt.pie(df['marks'],labels=df['student_name'])  # create pie chart with marks as value and name as label.

