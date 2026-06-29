import pandas as pd
pd.set_option('display.max_colwidth',None)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
df = pd.read_csv('healthcare_dataset.csv')
print(df.columns)

blood_typ = df.groupby('Blood Type')['Test Results'].count()
blood_typ.sort_values(ascending=False,inplace=True)
print('Here is a list which shows number of patients based on the blood group')
print(blood_typ.to_list())