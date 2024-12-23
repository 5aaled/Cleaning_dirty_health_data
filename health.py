from tkinter.ttk import Treeview

import numpy as np
import pandas as  pd ,  seaborn as sns , matplotlib.pyplot as plt


df = pd.read_csv('~/Documents/kaggel/dirty_health_data.csv')

print(df.info())
df[['first_name','last_name']] = df['Name'].str.split(' ' ,expand = True)
df['first_name'] = df['first_name'].str.capitalize()
df['last_name'] = df['last_name'].str.capitalize()
df['full_name'] = df['first_name'] + ' ' + df['last_name']
## age ##
df['Age'] = df['Age'].apply(lambda x: x if 1 <= x <= 125 else np.nan)
df['Age'] = df['Age'].fillna(df['Age'].median()) # median is better than mean
########
df['Gender'] = df['Gender'].map({'M' : 'Male' , 'F' : 'Female' ,'Unknown' : np.nan})
df['Visit Date'] = pd.to_datetime(df['Visit Date'] ,format='mixed',errors='coerce')
df['Heart Rate'] =  df['Heart Rate'].apply(lambda x  : x if  1 <= x <= 125 else np.nan)
df['Heart Rate'] = df['Heart Rate'].fillna(df['Heart Rate'].median()) # medain is better than mean in thiz case

#### diagonsis
df['Diagnosis'] = df['Diagnosis'].str.strip().str.capitalize()
df['Diagnosis'] = df['Diagnosis'].str.replace('Dibetes' ,'Diabetes')
print(df['Diagnosis'].value_counts())
### cleaning hospital columns
df['Hospital'] = df['Hospital'].replace({'city hospital' : 'City Hospital' ,'city hosp.' :'City Hospital','GENERAL CLINIC' : 'General Clinic'})
### there is some other ways
# df['Hospital'] = df['Hospital'].str.lower().str.strip()  # Lowercase and strip spaces.
# df['Hospital'] = df['Hospital'].str.replace(r'\b(city hospital|city hosp\.)\b', 'City Hospital', regex=True)
# df['Hospital'] = df['Hospital'].str.replace(r'\b(general clinic|general clinic)\b', 'General Clinic', regex=True)
# df['Hospital'] = df['Hospital'].str.title()  # Final capitalization
df['Costs'] = df['Costs'].str.replace(r'\D' ,'',regex = True).astype('float64')
df['Costs'] = df['Costs'].apply(lambda x : np.nan if x <0 else x)
df['Costs'] = df['Costs'].fillna(df['Costs'].median())
#print(df[['Age', 'Heart Rate']].describe())
sns.histplot(data=df, x='Age', kde=True, bins=20)
plt.title('Age Distribution')
plt.show()








