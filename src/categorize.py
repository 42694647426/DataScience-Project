import pandas as pd
from tqdm import tqdm

df = pd.read_csv ('data/clear_tweets.tsv',sep='\t', index_col=False)

for index, row in tqdm(df.iterrows()):
    #print(row["Twitts"])
    if "omicron" in row["Twitts"].lower():
        df.at[index, "Topic"] = "O"
    elif any(x in row["Twitts"].lower() for x in ["vaccine", "passport", "pfizer", "moderna", "johnson"]):
        df.at[index, "Topic"] = "V"
    elif any(x in row["Twitts"].lower() for x in ["news", "policies", "quarantine", "government", "positive"]):
        df.at[index, "Topic"] = "N"
    elif any(x in row["Twitts"].lower() for x in ["symptoms", "life", "job", "change", "experience"]):
        df.at[index, "Topic"] = "I"
    elif any(x in row["Twitts"].lower() for x in ["want to", "hate", "ridiculous", "like", "doubt"]):
        df.at[index, "Topic"] = "E"
    else:
        # cannot be categorized
        df.at[index, "Topic"] = None
    
    if any(x in row["Twitts"].lower() for x in ["want to", "like", "excellent", "love", "great", "happy"]):
        df.at[index, "Sentiment"] = "P"
    elif any(x in row["Twitts"].lower() for x in ["hate", "crazy", "ridiculous", "afraid", "doubt", "sad"]):
        df.at[index, "Sentiment"]  = "N"
    else:
        df.at[index, "Sentiment"]  = None

print(df.head())
df.to_csv("data/clear_twitts_anno.tsv", sep="\t", index=False)