
import requests
import tweepy 
import json
import pandas as pd
import importlib as ip



acesso = ip.import_module('acesso')








class Boletim(): 
	def __init__(self,casos,mortes):
	 self.date = df['date']
	 self.confirmed = casos
	 self.deaths = mortes

	def appendBoletim(self): 
		print("confirmados: " + str(self.confirmed))
		print("mortes: " + str(self.deaths))
		data = pd.DataFrame({'date':[self.date],'confirmed':[self.confirmed],'deaths':[self.deaths]}, index=[self.count])
		data.to_csv('boletins.csv',mode='a', header=False)





def calcula(): 
	mortes = df['newDeaths'].iloc[0]

	casos = df['newCases'].iloc[0]
	print(mortes)
	tuitar(mortes,casos)
	

def tuitar(mortes,casos): 

	mensagem = "Hoje, foram registradas "+ str(mortes) +" mortes por Covid-19 no ES e " + str(casos) + " novos casos."
	try: 
		api.update_status(mensagem)
		print("tuitou")
	except: 
		print("status não foi atualizado")	
	
	#doc = Boletim(casos,mortes)
	#doc.appendBoletim() 
	gerarJSON()


def gerarJSON(): 
	df.to_csv('anterior.csv')
	print("gravou")




consumer_key = acesso.CONSUMER_KEY
consumer_secret = acesso.CONSUMER_SECRET
access_token = acesso.ACCESS_TOKEN
access_token_secret = acesso.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.me()
print (user.name)

requisicao = 'https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv'

df = pd.read_csv(requisicao)


	
df = df.loc[(df['state']=='ES')]
df = df.loc[(df['date']==df['date'].max())]
df = df.reset_index()
print(df.head())


calcula()






	
	