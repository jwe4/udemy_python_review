from database import CursorFromConnectionFromPool

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
            cursor.execute('insert into users (email,first_name, last_name, oauth_token, oauth_token_secret) values (%s,%s,%s,%s,%s)',
                           (self.email, self.first_name, self.last_name, self.oauth_token, self.oauth_token_secret))


    @classmethod
    def load_from_db_by_email(cls, email):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('select * from users where email=%s', (email,)) #needs a tuple
            user_data = cursor.fetchone()
            return cls(email=user_data[1], first_name=user_data[2],
                       last_name=user_data[3], oauth_token=user_data[4],
                       oauth_token_secret=user_data[7], id=user_data[0])