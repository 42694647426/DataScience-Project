import tweepy

br = 'PUT YOU ACCOUNT BEARER TOKEN'
client = tweepy.Client(bearer_token=br)

# Replace with your own search query
query = 'COVID -is:retweet lang:en'

# Replace with time period of your choice
start_time = '2021-12-01T00:00:00Z'

# Replace with time period of your choice
end_time = '2021-12-02T00:00:00Z'

with open('raw_tweets.txt', 'a+') as filehandle:
    # Replace the limit=1000 with the maximum number of Tweets you want
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                              start_time=start_time, end_time=end_time,
                              tweet_fields=['context_annotations', 'created_at'],
                              max_results=100).flatten(limit=500):
        filehandle.write('%s\n' % tweet.text.replace("\n",'. '))
