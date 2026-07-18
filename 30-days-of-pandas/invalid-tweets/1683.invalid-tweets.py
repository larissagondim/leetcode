import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalid = []
    for i in range(len(tweets['content'])):
        if(len(tweets['content'][i]) > 15):
            invalid.append(tweets['tweet_id'][i])

    dfinvalid = pd.DataFrame({
        "tweet_id": invalid
    })
    return dfinvalid
    
# solução mais idiomática:

# import pandas as pd

# def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
#     return tweets.loc[tweets['content'].str.len() > 15, ['tweet_id']]
    