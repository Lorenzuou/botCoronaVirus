
import requests
import tweepy 
import json
import pandas as pd
import importlib as ip
from decouple import config

totalMortes = 0
totalCasos = 0


class Data(): 
    def __init__(self,count,confirmados,mortes):
        self.count = count
        self.confirmados = confirmados 
        self.mortes = mortes 



def calcula(): 
	totalMortes = dfAtual.loc[dfAtual.last_valid_index(),'deaths'] - dfAnterior.loc[dfAnterior.last_valid_index(),'deaths']

	totalCasos = dfAtual.loc[dfAtual.last_valid_index(),'confirmed'] - dfAnterior.loc[dfAnterior.last_valid_index(),'confirmed']
	tuitar()

def tuitar(): 
	
	
	
	mensagem = "Hoje foram registradas "+ str(totalMortes) +" mortes por corona virus no ES e " + str(totalCasos) + " novos casos."
	api.update_status(mensagem)
	print("tuitou")
	gerarJSON()


def gerarJSON(): 
	df.to_json('anterior.json')
	a_file = open("count.json", "w")
	json.dump(a['count'], a_file)
	a_file.close()
	print("gravou")



acesso = ip.import_module('acesso')

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
	df = df.loc[(df['state'] == 'ES')]
	df = df.reset_index()
	df.to_json('atual.json')

	dfAnterior = pd.read_json('anterior.json')
	dfAtual = pd.read_json('atual.json')
	


	print(dfAtual.loc[dfAtual.last_valid_index(),'date'])
	print(dfAnterior.loc[dfAnterior.last_valid_index(),'date'])
	print(dfAnterior.loc[dfAnterior.last_valid_index(),'confirmed'])

	print(dfAtual.loc[dfAtual.last_valid_index(),'confirmed'])
	if dfAtual.loc[dfAtual.last_valid_index(),'date'] != dfAnterior.loc[dfAnterior.last_valid_index(),'date'] and dfAtual.loc[dfAtual.last_valid_index(),'confirmed'] > dfAnterior.loc[dfAnterior.last_valid_index(),'confirmed']:
		calcula()
	else: 
		print('Não atualizaram os números do ES ainda')
		
else: 
	print("Não atualizaram o boletim ainda")	







	
	