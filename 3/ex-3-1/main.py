import pandas as pd

columns = ['name', 'city', 'age', 'exam-score']
df = pd.read_csv('data3.csv', names=columns)
print(df)
print('\n')

print(df.head(n=2))
print('\n')
print(df.tail(n=2))
print('\n')

print(df.city)
print('\n')

print(df.city[3])
print('\n')

print(df.loc[3])
