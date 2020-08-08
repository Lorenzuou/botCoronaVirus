import tweepy 
import requests
import json
import pandas as pd
from pandas.io.json import json_normalize


consumer_key = 'JleMtnscCGO25BUM4ms7AHtB9'
consumer_secret = '7mxE5EjyxlqcpcbBoiUxOAJEAS6QlBWuBtYDa13NdiuipYScfU'
access_token = '1291179065093885952-Bx0085BS0ak8fAjJSaJO9jStSOPFrc'
access_token_secret = 'DVkGuzS2wXoxmPLviNPfaeCvL9eL5aHkDVODImaThgul7'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.me()
print (user.name)

for follower in tweepy.Cursor(api.followers).items():    
	follower.follow()    
	print ("Followed everyone that is following " + user.name)


r = requests.get('https://brasil.io/api/dataset/covid19/caso/data/?format=json')


a = json.loads(r.text)
df = json_normalize(a, ['results'])
df = df.loc[(df['state'] == 'ES')]

print(df.head())
