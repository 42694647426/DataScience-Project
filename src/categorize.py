import pandas as pd
from tqdm import tqdm

df = pd.read_csv('./data/clear_twitts.tsv',sep='\t', index_col=False)
df = df.astype({"Topic":str})
df = df.astype({"Sentiment":str})
print(type(df.at[5, "Topic"]))

for index, row in tqdm(df.iterrows()):
    #print(row["Twitts"])

    if any(x in row["Twitts"].lower() for x in ["omicron", "variant"]):
        df.at[index, "Topic"] = "O"
    elif any(x in row["Twitts"].lower() for x in ["vaccine", "vac", "vax", "passport"]):
        df.at[index, "Topic"] = "V"
    elif any(x in row["Twitts"].lower() for x in ["news", "policy", "policies", "quarantine", "government", "positive"]):
        df.at[index, "Topic"] = "N"
    elif any(x in row["Twitts"].lower() for x in ["symptom", "life", "job", "change", "experience", "become"]):
        df.at[index, "Topic"] = "I"
    elif any(x in row["Twitts"].lower() for x in ["think", "hate", "die", "like", "afraid"]):
        df.at[index, "Topic"] = "P"
    else:
        # cannot be categorized
        df.at[index, "Topic"] = None
    
    if any(x in row["Twitts"].lower() for x in ["want to", "hope", "excellent", "love", "great", "happy"]):
        df.at[index, "Sentiment"] = "P"
    elif any(x in row["Twitts"].lower() for x in ["hate", "crazy", "ridiculous", "afraid", "doubt", "sad"]):
        df.at[index, "Sentiment"] = "N"
    else:
        df.at[index, "Sentiment"] = None

print(df.head())
df.to_csv("./data/new_clear_twitts_anno.tsv", sep="\t", index=False)