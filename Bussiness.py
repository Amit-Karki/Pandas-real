import pandas as pd 

df = pd.read_excel("intl_business.xlsx")
#df.columns returns all columns in the dataframe like Customer_id
print(df.columns) 
# Our column name is incomplete and in shortform like inv_no So we must change it 
df.rename(columns={
    'cos_id': 'Customer_id',
    'inv_day': 'invoice_day',
    'Descrip': 'Product_details',
    'inv_no': 'invoice_number',
    'Stck_code':'Stock_code',
    'Trans_has':'Transaction_history',
    'Cst_chrt': 'Customer_chort',
    'cm_guid': 'Complete_guide'
},inplace=True)
#We are checking for data types of all columns and if it not apporpriate like invoice day in string we may change it to appropraite type 
print(df.dtypes)
#We checked for data type of all column and its type is as except like country in string,quantity in integer etc.
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