# Task NumPy

import pandas as pd

kn4_file = pd.read_excel('KN-4.xlsx')
print(kn4_file)

print(kn4_file.shape)
print(kn4_file.columns)

print(kn4_file.loc[kn4_file['Student'] == 'Андрух Ігор'])

kn4_file.fillna(0, inplace=True)
print(kn4_file)

kn4_file['Test'] = kn4_file['Test'] * 12 / 100
print(kn4_file)

kn4_file['Lab1'] = kn4_file['Lab1'].map({'+': 2, '/': 1, 0: 0})
kn4_file['Lab2'] = kn4_file['Lab2'].map({'+': 2, '/': 1, 0: 0})
print(kn4_file)

kn4_file['L7'] = kn4_file['Lab7'].str.split('/', expand=True)[0]
print(kn4_file)

kn4_file['L7'] = pd.to_numeric(kn4_file['L7'])
print(kn4_file)

kn4_file['Result'] = kn4_file[['Lab1', 'Lab2', 'Test', 'L7']].sum(axis=1)
print(kn4_file)

kn4_file = kn4_file.rename(columns={'L7': 'L71'})
print(kn4_file)

print(kn4_file['Result'].max(axis=0))

print(kn4_file['Result'].argmax())

print(kn4_file.iloc[[kn4_file['Result'].argmax()], 0])

print(kn4_file.loc[kn4_file['Result'] == 0.00]['Student'])

print(kn4_file.loc[kn4_file['Result'] > 15.00]['Student'])

print(len(kn4_file.loc[kn4_file['Result'] > 15.00]['Student']))

kn4_file = kn4_file.sort_values(by=['Result'], ascending=False)
print(kn4_file)

print(kn4_file[kn4_file['Lab1'].isin([2,1])]['Student'])

kn4_file.insert(8, "лаб4", 2, True)
print(kn4_file)

print(kn4_file[['Student', 'Result']])

kn4_file['Zdano'] = kn4_file['Result'].apply(lambda x: 'dopusk' if x > 15 else 'talon')
print(kn4_file)

print(kn4_file[kn4_file['Zdano'].isin(['dopusk'])]['Student'])

#########################################