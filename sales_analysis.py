import pandas as pd
pd.set_option('display.max_columns',None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 199999)
df = pd.read_csv('sales_data.csv')
print(df)