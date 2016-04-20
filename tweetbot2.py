from twython import Twython
import csv

CONSUMER_KEY = 'Janbon4bSacjLP2RUVeHz2UoY'
CONSUMER_SECRET = 'ttAnmMWLy1GsbUCdkZY2unCP1VgD1eMWIpOQQtO387Yt6uRa2P'
ACCESS_TOKEN = '722878958702690304-A5m3Zpyk6tX7GVIzEasaBtQrz7WrTn8'
ACCESS_TOKEN_SECRET = '3wxSmW0ezDKSyFTrt1uVvacctb6uFDx9BVXkCkYcNZvMb'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

search = twitter.search(q='seltzer', count="100")
tweets = search['statuses']

with open ('data.csv', 'w') as fp:
    a = csv.writer(fp)

#Open the CSV file. 'data.csv' can be renamed to whatever you would like. This is the filename it will save under.

    a.writerow(('Search Term', 'Tweet Text', 'URL'))

#At the top of the CSV file, we want to add in a row with columns labeled 'Search Term' and 'Tweet Text'.

    for result in tweets:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        text=[['seltzer', result['text'].encode('utf-8'), url]]
        a.writerows((text))
