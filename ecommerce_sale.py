import pandas as pd
import pandas as pd
import numpy as np
pd.set_option('display.max_columns',None)

pd.set_option("display.max_rows", None)
pd.set_option("display.width", 199999)
df = pd.read_csv('A:\Downloads\Github_Demo\Pandas-real\ecommerce.csv')
print(df.columns)
print(df.head())
print(df.isnull().sum())
print(df.dtypes)
print(df['region'].unique())

#order_date is in str type so we should convert it to date time
df['order_date'] = pd.to_datetime(df['order_date'])
df['Profit'] = ((df['quantity'] * df['unit_price']) - (df['discount_percent']/100 * df['quantity'] * df['unit_price'])) - df['unit_cost'] * df['quantity'].sort_values()

category = ['North America','Europe','South America','Asia']
x = df.groupby([df['region'],df['category'],df['product']])['Profit'].sum()
x_df = x.reset_index()

z = x_df.sort_values(by=['region','Profit'],ascending=[True,False])
z['region'] = z['region'].mask(z['region'].duplicated(),'')
z['category'] = np.where(z['category'] == z['category'].shift(), ' ', z['category'])
print(z)