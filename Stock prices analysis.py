import pandas as pd
pd.set_option('display.max_columns', None)
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('A:\\Downloads\\Github_Demo\\Pandas-ral\\goldstock v1.csv', parse_dates=['Date'], index_col='Date')
print(df.head())
# We saw there is one unnecessary column, which is not named so we weill remove it from the dataframe.
df.drop(columns=['Unnamed: 0'], inplace=True)
print(df.head())
# our goal is to see the stock prices growing over monthly basis

df['Stock growth'] = ((df['Close'] - df['Open']) / df['Open']) * 100

x = df['Stock growth'].resample('ME').mean()
x = x.to_frame(name='Stock growth')
x['Month'] = x.index.month
x['Year'] = x.index.year
print(x.index)

sns.relplot(
    data=x,
    kind='line',
    x='Month',
    y='Stock growth',
    col='Year',
    col_wrap=3, 
    height=3,
    aspect=1.2
)

plt.show()