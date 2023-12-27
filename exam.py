import numpy as nm
import pandas as pd

df = pd.read_excel('exam.xlsx')

# 1 задание
streets = df.loc[(df['Формат магазина']=='Street') & (df['Выборка'] == 'Тестовая')]
streets1 = df.loc[(df['Формат магазина']=='Strееt') & (df['Выборка'] == 'Тестовая')]
streets2 = df.loc[(df['Формат магазина']=='Стрит') & (df['Выборка'] == 'Тестовая')]
streets3 = df.loc[(df['Формат магазина']=='Стрт') & (df['Выборка'] == 'Тестовая')]
result = streets['Формат магазина'].count() + streets2['Формат магазина'].count() + streets3['Формат магазина'].count() + streets1['Формат магазина'].count()
print('Сколько магазинов стрит : ' , result)

# 2 задание
df_info = pd.read_excel('exam.xlsx', sheet_name='Справочник точек')
df_revenue = pd.read_excel('exam.xlsx', sheet_name='Выручка по обучающей выборке', usecols="A,N:Y")
df_merged = pd.merge(df_info, df_revenue, on='id точки')
miniMagaz1 = df_merged.loc[(df_merged['Формат магазина'] == 'Мини ТЦ') ,'2016-01-01':'2016-12-01']
avg_rev = miniMagaz1.mean().sum()
print(avg_rev)

# 3 заданте
parking = df.loc[df['Парковка'] == 'бесплатная парковка']
parking2 = df.loc[df['Парковка'] == 'бесплатная паpковка']
free_parking = parking['Парковка'].count() + parking2['Парковка'].count()
print('Магазин бесплатная парковка : ', free_parking)