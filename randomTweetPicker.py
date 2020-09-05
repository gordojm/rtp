import tweepy
import random
import local_settings

access_token = local_settings.access_token
access_token_secret = local_settings.access_token_secret
consumer_key = local_settings.consumer_key
consumer_secret = local_settings.consumer_secret

tweets_list = []

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def get_random_tweet(user):
    if(user in local_settings.ignored_accounts):
        random_tweet = '*Función deshabilitada para la cuenta*'
        print(random_tweet)
        return random_tweet
    else:
        tweets_list.clear()
        for status in tweepy.Cursor(api.user_timeline, screen_name=str(user), tweet_mode="extended").items(50000):
            if (not status.retweeted and 'RT @' not in status.full_text):
                tweets_list.append(status.full_text)
                if len(tweets_list) >= 100:
                    print(tweets_list)
                    random_tweet = f'{random.choice(tweets_list)}'
                    print(random_tweet)
                    return random_tweet
                else:
                    random_tweet = 'Error: el usuario no existe, está suspendido o no se encontraron tweets originales'
                    print('error')
                # get_random_tweet()

                # print(tweets_list)
