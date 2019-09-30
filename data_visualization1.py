
#imporantly pandas is amazing
import pandas as pd
import matplotlib.pyplot as plt

# This function can read from system
df=pd.read_csv('student.csv')       # make a data frame

plt.pie(df['marks'],labels=df['student_name'])  
# create pie chart with marks as value and name as label.

