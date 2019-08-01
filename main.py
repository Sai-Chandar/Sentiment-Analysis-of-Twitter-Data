import tweepy
from hidden import *                                           #import keys from hidden.py
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import argparse
def twitter_Authentication():                                  #Twitter API authentication
    global api
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)  #Make sure to enter Consumer key, consumer secret
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)   #access token, access token secret in hidden.py
    api = tweepy.API(auth)

def hashtag_search(hashtag):                                   #Searches through the hashtag and returens args.num tweets
    tweets = tweepy.Cursor(api.search, q= hashtag, tweet_mode = 'extended', result_type = 'mixed').items(args.num)
    return tweets
def User_comment_search(user_name):                            #Searches  through comments of a user tweet and returns a list of tweets
    tweets = list()
    recent_tweet = tweepy.Cursor(api.user_timeline, user_name).items(args.num)
    for full_tweet in recent_tweet:
        for tweet in tweepy.Cursor(api.search, q="to:"+user_name, tweet_mode = 'extended', result_type = "recent").items(1000):
            if hasattr(tweet, 'in_reply_to_status_id_str'):
                if tweet.in_reply_to_status_id_str == full_tweet.id_str:
                    return tweets.append(tweet)

def Sentiment_scores(tweets):                                  #Sentiment scores using vader lexicon for the tweets
        Analyzer = SentimentIntensityAnalyzer()
        for tweet in tweets:
            vs = Analyzer.polarity_scores(tweet.full_text)
            print(vs['compound'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-ht","--hashtag", help = "Enter a hashtag", type = str)
    group.add_argument("-u","--user_name",help = 'Enter user name', type = str)
    parser.add_argument("-n","--num", help = "Number of recent tweets to be analysed", default = 1, type = int)
    args = parser.parse_args()
    twitter_Authentication()
    if args.hashtag:
        if not '#' in args.hashtag or ' ' in args.hashtag:
            print("This is not a hashtag!")
        tweets = hashtag_search(args.hashtag)
        Sentiment_scores(tweets)
    if args.user_name:
        tweets = User_comment_search(args.user_name)
        Sentiment_scores(tweets)
