
import requests
import tweepy 
import json
import pandas as pd
import importlib as ip
from decouple import config



acesso = ip.import_module('acesso')








class Boletim(): 
	def __init__(self,casos,mortes):
		self.count = a['count']
		self.date = dfAtual.loc[dfAtual.last_valid_index(),'date']
		self.confirmed = casos
		self.deaths = mortes

	def appendBoletim(self): 
		print("confirmados: " + str(self.confirmed))
		print("mortes: " + str(self.mortes))
		data = pd.DataFrame({'count':[self.count],'date':[self.date],'confirmed':[self.confirmed],'deaths':[self.deaths]})
		data.to_csv('boletins.csv',mode='a', header=False)





def calcula(): 
	mortes = dfAtual.loc[dfAtual.last_valid_index(),'deaths'] - dfAnterior.loc[dfAnterior.last_valid_index(),'deaths']

	casos = dfAtual.loc[dfAtual.last_valid_index(),'confirmed'] - dfAnterior.loc[dfAnterior.last_valid_index(),'confirmed']


	doc = Boletim(casos,mortes)


	tuitar(casos,mortes)
	

def tuitar(casos,mortes): 
	mensagem = "Hoje, foram registradas "+ str(mortes) +" mortes por Covid-19 no ES e " + str(casos) + " novos casos."
	try: 
		api.update_status(mensagem)
		print("tuitou")
	except: 
		print("status não foi atualizado")	
	
	
	doc.appendBoletim() 
	gerarJSON()


def gerarJSON(): 
	df.to_json('anterior.json')
	a_file = open("count.json", "w")
	json.dump(a['count'], a_file)
	a_file.close()
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

requisicao = requests.get('https://brasil.io/api/dataset/covid19/caso/data/?format=json')
a = json.loads(requisicao.text)


f = open('count.json')
f = json.load(f)



if a['count'] > f:
	df = pd.json_normalize(a, ['results'])
	print(df)
	df = df.loc[(df['state'] == 'ES')]
	df = df.reset_index()
	df.to_json('atual.json')
	
	dfAnterior = pd.read_json('anterior.json')
	dfAtual = pd.read_json('atual.json')
	
	print(dfAtual)
	
	
	print(dfAtual.loc[dfAtual.last_valid_index(),'confirmed'])
	
	if dfAtual.loc[dfAtual.last_valid_index(),'date'] != dfAnterior.loc[dfAnterior.last_valid_index(),'date'] and dfAtual.loc[dfAtual.last_valid_index(),'confirmed'] > dfAnterior.loc[dfAnterior.last_valid_index(),'confirmed']  :
	
		calcula()

	else: 
		print('Não atualizaram os números do ES ainda')
		
else: 
	print("Não atualizaram o boletim ainda")	







	
	