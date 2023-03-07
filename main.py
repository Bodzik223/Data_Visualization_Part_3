import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_can = pd.read_excel(
    "Canada.xlsx",
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True) #Видалення стовпців

df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True) #зміна назв деяких стовпців

df_can['Total'] = df_can[[1980,       1981,       1982,
             1983,       1984,       1985,       1986,       1987,       1988,
             1989,       1990,       1991,       1992,       1993,       1994,
             1995,       1996,       1997,       1998,       1999,       2000,
             2001,       2002,       2003,       2004,       2005,       2006,
             2007,       2008,       2009,       2010,       2011,       2012]].sum(axis=1) # Додаваннянового стовпця для підсумку загальної кількість іммігрантів за країнами за весь період 1980-2013 років



df_can.set_index('Country', inplace=True) # Встановлення індексом Country

df_can.columns = list(map(str, df_can.columns)) # Перетворення назв стовпців у з int у string

years = list(map(str, range(1980, 2014))) # Створення змінної для доступу до стовпців

# Побудова регресії кілкьість емігрантів на рік
df_tot = pd.DataFrame(df_can[years].sum(axis=0)) # Обраховуємо кількість емігрантів кожного року

df_tot.index = map(float, df_tot.index)

df_tot.reset_index(inplace=True)

df_tot.columns = ['year', 'total']

plt.figure(figsize=(15, 10))

sns.set(font_scale=1.5)

ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='*', scatter_kws={'s': 200})
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigration to Canada from 1980 - 2013')

# plt.savefig('1.png')
plt.show()

# Побудова регресії кілкьість емігрантів з Данії, Швеції та Норвегії до Канади з 1980 по 2013 рік.

df_countries = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()

df_total = pd.DataFrame(df_countries.sum(axis=1))

df_total.reset_index(inplace=True)

df_total.columns = ['year', 'total']

df_total['year'] = df_total['year'].astype(int)

plt.figure(figsize=(15, 10))

sns.set(font_scale=1.5)
sns.set_style('whitegrid')

ax = sns.regplot(x='year', y='total', data=df_total, color='blue', marker='*', scatter_kws={'s': 200})
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigrationn from Denmark, Sweden, and Norway to Canada from 1980 - 2013')

# plt.savefig('2.png')
plt.show()