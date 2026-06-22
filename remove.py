print("Before:", len(df))

df.drop_duplicates(inplace=True)

print("After:", len(df))
