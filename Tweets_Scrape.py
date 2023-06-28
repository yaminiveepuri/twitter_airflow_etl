import snscrape.modules.twitter as sntwitter
import pandas as pd

def twitter_etl():
    tweets = []
    for tweet in sntwitter.TwitterSearchScraper('"cocacola lang:en near:"United States""').get_items():
        if tweet.place is not None:
            tweets.append(tweet)
        if len(tweets) == 5000:
            break

    cocacola_data = pd.DataFrame(tweets , columns = ['date','rawContent','coordinates','place'])
    cocacola_data.to_csv("cocacola_tweets.csv")

    pepsi_tweets = []
    for tweet in sntwitter.TwitterSearchScraper('"pepsi lang:en near:"United States""').get_items():
        if tweet.place is not None:
            pepsi_tweets.append(tweet)
        if len(pepsi_tweets) == 5000:
            break

    pepsi_data = pd.DataFrame(pepsi_tweets, columns = ['date','rawContent','coordinates','place'])
    pepsi_data.to_csv("pepsi_tweets.csv")