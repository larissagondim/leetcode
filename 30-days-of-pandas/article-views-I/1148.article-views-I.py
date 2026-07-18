import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    ids = []

    for i in range(len(views['viewer_id'])):
        if (views['author_id'][i] == views['viewer_id'][i]) and (views['author_id'][i] not in ids):
            ids.append(views['author_id'][i])

    ids.sort()

    return pd.DataFrame({"id": ids})