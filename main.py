from helper_functions import reddit_csv_to_df, twitter_csv_to_df


def main():
    reddit_pro_choice = reddit_csv_to_df('data/Copy of Draft Data_Reddit - Prochoice subreddit .csv')
    reddit_pro_life = reddit_csv_to_df('data/Copy of Draft Data_Reddit - Prolife subreddit .csv')
    twitter_tweets = twitter_csv_to_df('data/Tweets.csv')


    print(reddit_pro_choice)


if __name__ == '__main__':
    main()
