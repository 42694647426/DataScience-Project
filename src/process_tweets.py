import pandas as pd

df = pd.read_csv ('raw_tweets.txt',sep='\t')
df = df.drop_duplicates(keep=False)
df = df.sample(n = 1000)
df['Topic'] = 'TOPIC'
df['Sentiment'] = 'SENTIMENT'
df.to_csv("clear_twitts.tsv", sep="\t")
