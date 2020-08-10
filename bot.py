import tweepy 
import requests
import json
import pandas as pd
import importlib as ip
from decouple import config

totalMortes = 0
totalCasos = 0

acesso = ip.import_module('acesso')


def calcula(): 
	totalMortes = df.loc[df.last_valid_index(),'deaths'] - dfAnterior.loc[df.last_valid_index(),'deaths']

	totalCasos = df.loc[df.last_valid_index(),'confirmed'] - dfAnterior.loc[df.last_valid_index(),'confirmed']
	tuitar()

def tuitar(): 
	mensagem = "Hoje foram registradas "+ str(totalMortes) +" mortes por corona virus no ES e " + str(totalCasos) + " novos casos."
	api.update_status(mensagem)
	print("tuitou")
	gerarJSON()


def gerarJSON(): 
	df.to_json('anterior.json')
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
df = pd.json_normalize(a, ['results'])
df = df.loc[(df['state'] == 'ES')]
df = df.reset_index()
df.to_json('atual.json')

dfAnterior = pd.read_json('anterior.json')
dfAtual = pd.read_json('atual.json')


if df.loc[df.last_valid_index(),'date'] == dfAnterior.loc[df.last_valid_index(),'date']:
     print('nao atualizaram os números ainda')
else: 
	calcula()
