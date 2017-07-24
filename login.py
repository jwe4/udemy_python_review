import constants
import oauth2
import urllib.parse as urlparse
import json


# Create a consumer, which uses CONSUMER_KEY and CONSUMER_SECRET to identify our app uniquely
consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET)
client = oauth2.Client(consumer)


# Uset the client to perform a request for the request token
response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')

if response.status != 200:
    print('An error occurred getting the request token from Twitter!')


# Get the request token parsing the query string returned
request_token = dict(urlparse.parse_qsl(content.decode('utf-8')))

# www.oursite.com 'login with twitter button'
#they presss 'sign in' or 'authorize
# Twitter sends them back to e.g. www.ourwebsite.com/auth
# we get that auth code + request token -> twitter -> access token

# don't have web site yet so get a token

# Ask the user to authorize our app and give us the pin code
print("Go to following site in your browser:")
print("{}?oauth_token={}".format(constants.AUTHORIZATION_URL, request_token['oauth_token']));

oauth_verifier = input("What is the PIN? ")

# Create a Token object which contains the request token and the verifier
token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)

# Create a client with our consumer (our app) and the newly created (and verified) token
client = oauth2.Client(consumer, token)

# Ask Twitter for an access token, and Twitter knws it should gus it becuase we've verified the request token
response, content = client.request(constants.ACCESS_TOKEN_URL, 'POST')
access_token = dict(urlparse.parse_qsl(content.decode('utf-8')))
print(access_token)

# Create an 'authorized_token' Token object and use that to perform Twitter API calls on behalf oth the user
authorized_token = oauth2.Token(access_token['oauth_token'], access_token['oauth_token_secret'])
authorized_client = oauth2.Client(consumer, authorized_token)

#Make Twitter API calls!
response, content = authorized_client.request('https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images','GET')


if response.status != 200:
    print("An error occurred")

# print(content.decode('utf-8'))
tweets = json.loads(content.decode('utf-8'))
for tweet in tweets['statuses']:
    print(tweet['text'])
