import pandas as pd


def reddit_csv_to_df(filepath):
    df = pd.read_csv(filepath)
    print(df.info)
    print(df.columns)

    clean_df = pd.DataFrame()
    clean_df['post'] = df['comments.comment']
    clean_df.insert(0, 'source', 'REDDIT')
    clean_df['date'] = df['comments.date']

    return clean_df


def twitter_csv_to_df(filepath):
    df = pd.read_csv(filepath)
    print(df.info)
    print(df.columns)

    clean_df = pd.DataFrame()
    clean_df['post'] = df['tweet']
    clean_df.insert(0, 'source', 'TWITTER')
    clean_df['date'] = df['date']

    return clean_df