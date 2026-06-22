print(df.isnull().sum())

df.fillna(0, inplace=True)
