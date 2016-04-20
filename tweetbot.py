from twython import Twython, TwythonError

CONSUMER_KEY = 'Janbon4bSacjLP2RUVeHz2UoY'
CONSUMER_SECRET = 'ttAnmMWLy1GsbUCdkZY2unCP1VgD1eMWIpOQQtO387Yt6uRa2P'
ACCESS_TOKEN = '722878958702690304-A5m3Zpyk6tX7GVIzEasaBtQrz7WrTn8'
ACCESS_TOKEN_SECRET = '3wxSmW0ezDKSyFTrt1uVvacctb6uFDx9BVXkCkYcNZvMb'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

try:
    twitter.update_status(status='See how easy this was?')
except TwythonError as e:
    print e

# read from csv
