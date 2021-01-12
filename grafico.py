import matplotlib.pyplot as plt
import matplotlib.dates as dates
from datetime import datetime
import pandas as pd 


requisicao = 'https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv'
df = pd.read_csv(requisicao)

fig, ax1 = plt.subplots()

df = df.loc[(df['state']=='ES')]

print(df.head())
date = pd.to_datetime(df['date'])
plt.title("Casos e mortes diárias de covid-19 no ES desde o início da pandemia ")
ax2 = plt.twinx()

ax1.plot(date,df['newCases'].rolling(window=15).mean(),color="red")
ax2.plot(date,df['newDeaths'].rolling(window=15).mean(),color="blue")
ax1.set_ylabel('Casos', color='red')
ax2.set_ylabel('Mortes', color='blue')

plt.show()
plt.savefig("output.png")
#plt.plot(date,df['newDeaths'], secondary_y=True)
# plt.xlabel("Datas")