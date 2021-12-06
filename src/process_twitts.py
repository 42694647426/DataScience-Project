import pandas as pd

df = pd.read_csv ('raw_tweets.txt',sep='\t')
df = df.drop_duplicates(keep=False)
df = df[df.Twitts.str.count(' ').add(1) > 15]
df = df.sample(n = 1000)
df['Topic'] = ''
df['Sentiment'] = ''
df.to_csv("clear_twitts.tsv", sep="\t")
# random200 = df.sample(n = 200)
# random200.to_csv("../data/random_200_twitts.tsv", sep="\t")
