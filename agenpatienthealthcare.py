import pandas as pd

df = pd.read_csv('healthcare_dataset.csv')
print(df.head())

df['agegrp'] = pd.cut(df['Age'],bins=[0,18,35,60,100],labels=['child','Youth','senior','old'])
print('Here is the percentage of the patients based on their age group:')
print(df['agegrp'].value_counts(ascending=False,normalize=True) *100)