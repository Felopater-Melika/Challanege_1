import pandas as pd

columns = ['name', 'city', 'age', 'exam-score']
df = pd.read_csv('data3.csv', names=columns)
print(df)
print('\n')

member = pd.Series(data=['John', 'Boston', 34, 79], index=df.columns, name=10)
df = df._append(member)
print(df)
print('\n')

df = df.drop(10)
print(df)
print('\n')

df['midterm-score'] = [71, 72, 73, 74, 75, 76, 77, 78, 79, 50]
print(df)
print('\n')

df.insert(loc=2, column='position', value=['dba', 'analyst', 'developer', 'dba', 'analyst', 'developer', 'dba', 'dba', 'analyst', 'analyst'])
print(df)
print('\n')

df = df.drop('age', axis=1)
print(df)
print('\n')

df['total'] = (df['exam-score'] + df['midterm-score']) / 2
print(df)
print('\n')
