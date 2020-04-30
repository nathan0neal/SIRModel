import pandas as pd
'@author:NathanBouret'

url = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/csv'

data = pd.read_csv(url, delimiter=",", decimal=".")
data = data[["dateRep", "day", "cases", "deaths", "countryterritoryCode"]]
data = data[data["countryterritoryCode"] == "DEU"]
data.to_csv('rawdata2.csv', index=False, encoding='utf-8')

