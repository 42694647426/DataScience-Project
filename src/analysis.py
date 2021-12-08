import pandas as pd
from tqdm import tqdm

def bar_graph(df: pd.DataFrame):
    
    plt = df.groupby(["Topic", "Sentiment"]).count().unstack('Sentiment').plot.bar()
    plt.show()

if __name__ =="__main__":
    df = pd.read_csv('data/tweets_anno_700_to_1000.tsv',sep='\t', index_col=False, encoding= 'unicode_escape')
    bar_graph(df)

