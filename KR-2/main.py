# ------------------------------
# Readme
# Якщо після Shift + F10 вкладка у браузері не грузиться, тоді зробіть F5 для поточного вікна
# ------------------------------

# Підключення потрібних для роботи пакетів
import pandas as pd  # Зчитування даних

pd.options.mode.chained_assignment = None  # default='warn'

import plotly.express as px

import os

from colorama import init

# use Colorama to make Termcolor work on Windows too
init()
from termcolor import colored

from raceplotly.plots import barplot

print("------------------------------")

# print(colored('Викиди CO2 з 1960 по 2018 рік', 'blue', 'on_white').center(40))
print(colored('Викиди CO2 (метричні тонни на душу населення) - 1960-2018', 'blue').center(250))
print("------------------------------")

# Перегляд всіх датасетів у дослідженні
print(colored("Використані datasets у дослідженні:", 'green'))
for dirname, _, filenames in os.walk('datasets/'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Зчитування файлу
print("------------------------------")
print(colored("Таблиця з даними", 'green'))
co2_data_file = pd.read_csv('datasets/CO2_emissions_1960_2018.csv', index_col='Country Name')
print(co2_data_file)
print("------------------------------")

# Розмірність таблиці
print(colored("Розмірність таблиці", 'green'))
size_table = co2_data_file.shape
print(size_table)
print("------------------------------")

# Транспонування та занулення всіх некоректно заповненних стовпчиків
co2_df_tr = co2_data_file.transpose()
co2_df_tr.index = pd.to_datetime(co2_df_tr.index).year
co2_df_tr.fillna(0, inplace=True)  # Занулення
print(colored("Кінцевий варіант таблиці", 'green'))
print(co2_df_tr.head(10))
print("------------------------------")

# Відображення викиду CO2 в світі за період 1960-2018
fig_emissions_year = px.line(data_frame=co2_df_tr, x=co2_df_tr.index, y=['World'], markers=True, animation_frame=None,
                             title='Викиди CO2 в світі за період 1960-2018')
fig_emissions_year.layout.xaxis.title = "Роки"
fig_emissions_year.layout.yaxis.title = "Рівень CO2 в повітрі(метричні тонни на душу населення)"
fig_emissions_year.show()

# ------------------------------

# Таблиця зі стовпцями Country Name, Year, та сортування значень за роками
print(colored("Таблиця з даними(сортування за роками)", 'green'))
co2_data_file.head()
co2_data_file.reset_index(level=0, inplace=True)
co2_data_file_2 = co2_data_file.melt(id_vars=['Country Name'], var_name='Year').sort_values(by=['Year'])
print(co2_data_file_2.head())
print("------------------------------")

# Хороплет карта
fig_emissions_year_2 = px.choropleth(data_frame=co2_data_file_2[co2_data_file_2['Country Name'] != 'World'],
                                     locationmode='country names', locations='Country Name', color='value',
                                     animation_frame='Year', title='Викиди CO2 по країнах за роками',
                                     color_continuous_scale=px.colors.sequential.RdBu_r, range_color=(200, 0))
fig_emissions_year_2.show()
# ------------------------------

# Стовпчикова діаграма(горизонтальна)
fig_emissions_year_3 = barplot(df=co2_data_file_2[co2_data_file_2['Country Name'] != 'World'],
                               item_column='Country Name', value_column='value', time_column='Year', top_entries=10)
fig_emissions_year_4 = fig_emissions_year_3.plot(title='Гонка викидів вуглецю за країнами (з 1960 по 2018 рік)',
                                                 value_label='Value', item_label='Топ 10 країн')
fig_emissions_year_4.layout.xaxis.title = "Рівень CO2 в повітрі(метричні тонни на душу населення)"

fig_emissions_year_4.show()
# ------------------------------

# Графік box
country_col = co2_data_file_2[co2_data_file_2['Country Name'] != 'World'].groupby(
    by=['Country Name']).max().sort_values(by=['value'], ascending=False).head(10).index.to_list()
country_col.extend(['Ukraine', 'Germany'])

fig_emissions_year_5 = px.box(data_frame=co2_data_file_2[co2_data_file_2['Country Name'].isin(country_col)], x='value',
                              y='Country Name', color='Country Name',
                              title='Зміна викидів вуглецю за 12 найбільшими країнами')
fig_emissions_year_5.layout.xaxis.title = "Рівень CO2 в повітрі(метричні тонни на душу населення)"
fig_emissions_year_5.layout.yaxis.title = "Країна"
fig_emissions_year_5.show()
# ------------------------------
