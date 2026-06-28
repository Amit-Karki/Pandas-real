import pandas as pd
pd.set_option('display.max_colwidth',None)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
df = pd.read_csv("healthcare_dataset.csv")

df["Age Group"] = pd.cut(df["Age"], bins=[0,18,35,60,100], labels=["Child", "Young Adult", "Adult", "Senior"])
x = df.groupby('Age Group')["Billing Amount"].agg(Average = 'mean',Std = 'std')
x['diff'] = x['Average'] - x['Std']
print('if diff is +ve avg gives true insights but if not the data is inconsisent and have gaps')
print(x.sort_values(by='Average'))