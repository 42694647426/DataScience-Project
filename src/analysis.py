from matplotlib import colors
import pandas as pd
import matplotlib.pyplot as plt

def bar_graph(df: pd.DataFrame):

    #df.groupby(["Topic", "Sentiment"]).count().unstack('Sentiment').plot.bar()
    df_count = df
    df_count.loc[df_count["Topic"] == 'O', "Topic"] = "Omicron"
    df_count.loc[df_count["Topic"] == 'V', "Topic"] = "Vaccine"
    df_count.loc[df_count["Topic"] == 'N', "Topic"] = "News"
    df_count.loc[df_count["Topic"] == 'I', "Topic"] = "Influence"
    df_count.loc[df_count["Topic"] == 'P', "Topic"] = "Opinion"
    df_count.loc[df_count["Sentiment"] == 'P', "Sentiment"] = "Positive"
    df_count.loc[df_count["Sentiment"] == 'N', "Sentiment"] = "Negative"
    df_count.loc[df_count["Sentiment"] == 'E', "Sentiment"] = "Neutral"

    df_count = df_count.groupby(["Topic", "Sentiment"]).count().rename(columns={'Twitts':'Total Count'})
    print(df_count.head(5))
    df_count.unstack("Sentiment").plot.bar()
    plt.show()
    

if __name__ =="__main__":
    df = pd.read_csv('data/tweets_anno_700_to_1000.tsv',sep='\t', index_col=False, encoding= 'unicode_escape')
    bar_graph(df)

