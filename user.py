from database import CursorFromConnectionFromPool
import oauth2
from twitter_utils import consumer
import json
import constants
import urllib.parse as urlparse


class User:
    def __init__(self, email, first_name, last_name, oauth_token, oauth_token_secret, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret
        self.id = id

    def __repr__(self):
        return "<user: {}>".format(self.email)

    def save_to_db(self):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute(
                'insert into users (email,first_name, last_name, oauth_token, oauth_token_secret) values (%s,%s,%s,%s,%s)',
                (self.email, self.first_name, self.last_name, self.oauth_token, self.oauth_token_secret))

    @classmethod
    def load_from_db_by_email(cls, email):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('select * from users where email=%s', (email,))  # needs a tuple
            user_data = cursor.fetchone()
            if user_data:
                return cls(email=user_data[1], first_name=user_data[2],
                           last_name=user_data[3], oauth_token=user_data[4],
                           oauth_token_secret=user_data[5], id=user_data[0])

    def twitter_request(self, uri, verb='GET'):
        authorized_token = oauth2.Token(self.oauth_token, self.oauth_token_secret)
        authorized_client = oauth2.Client(consumer, authorized_token)

        # Make Twitter API calls!
        response, content = authorized_client.request(uri,verb)
        if response.status != 200:
            print("An error occurred")
        return json.loads(content.decode('utf-8'))

    def get_request_token(self):
        # Create a consumer, which uses CONSUMER_KEY and CONSUMER_SECRET to identify our app uniquely
        client = oauth2.Client(consumer)

        # Uset the client to perform a request for the request token
        response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')

        if response.status != 200:
            print('An error occurred getting the request token from Twitter!')

        # Get the request token parsing the query string returned
        return dict(urlparse.parse_qsl(content.decode('utf-8')))
