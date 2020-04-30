# permet de faire le webscrapping necessaire pour recuperer les donnees
'@author:NathanBouret'
import pandas as pd

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url2 = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
url3 = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'


def condition(index):
    if index == 121:  ##index de Germany
        return False
    else:
        return True


def condition2(index):
    if index == 113:  ##index de Germany
        return False
    else:
        return True


df = pd.read_csv(url, delimiter=",", decimal=".")
a=df.values[121]
df2 = pd.read_csv(url, delimiter=",", decimal=".")
b=df2.values[121]
df3 = pd.read_csv(url, delimiter=",", decimal=".")
c=df3.values[113]

df.to_csv('rawdata1.csv', index=False, encoding='utf-8')
df2.to_csv('rawdata1.csv', index=False, encoding='utf-8', mode='a')  # permet ecriture
df3.to_csv('rawdata1.csv', index=False, encoding='utf-8', mode='a')  # permet ecriture
