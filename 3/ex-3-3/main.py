import pandas as pd

columns = ['name', 'city', 'age', 'exam-score']
df = pd.read_csv('data3.csv', names=columns)

print("Our DataFrame:")
print(df)
print('\n')

sorted_df = df.sort_values('exam-score')
print("Our Sorted DataFrame:")
print(sorted_df)
print('\n')

filter = df['exam-score'] >= 80
print("All rows where the exam score was 80 or above:")
print(df[filter])
print('\n')

print("The mean exam score for all rows:")
print(df['exam-score'].mean())
