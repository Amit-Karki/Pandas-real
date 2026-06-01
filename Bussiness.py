import pandas as pd 

df = pd.read_excel("A:\\Downloads\\intl_business.xlsx")
#df.columns returns all columns in the dataframe like Customer_id
print(df.columns) 
print(df.dtypes)
#isnull checks for missing value in each column and sum tells total missing value in each column
print(df.isnull().sum())
#We checke and and there are no missing values but wait may be there is invalid data like unit_price in -ve so lets check
print(df.loc[df['Quantity'] <= 0,'Quantity'].sum())
print(df.loc[df['Unit_price'] <= 0,'Unit_price'].sum())
# We checked and there is no impossible data
# We are checking for list of all country from which our product is brought
print(list(df['Country'].unique()))
df['total_transaction'] = df['Quantity'] * df['Unit_price']
country_sales = df.groupby('Country')['total_transaction'].sum()
print(country_sales)
print('Here is the list of the European country through which maximum sale happened')
print(country_sales.sort_values(ascending=False))