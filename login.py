
from user import User
from database import Database
from twitter_utils import consumer, get_request_token, get_oauth_verifier, get_access_token

Database.initialise(user='postgres',
                    password='12345',
                    database='learning2',
                    host='localhost')

user_email = input("Enter your e-mail address: ")
user = User.load_from_db_by_email(user_email)
if not user:
    request_token = get_request_token()
    oauth_verifier = get_oauth_verifier(request_token)
    access_token = get_access_token(request_token, oauth_verifier)
    print(access_token)

    screen_name = input("Enter your screen name: ")

    user = User(screen_name,  access_token['oauth_token'], access_token['oauth_token_secret'])
    user.save_to_db();

tweets = user.twitter_request('https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images')
for tweet in tweets['statuses']:
    print(tweet['text'])
