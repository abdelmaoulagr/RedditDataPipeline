from etls.reddit_etl import connect_reddit
from utils.constants import CLIENT_ID, SECRET
from etls.reddit_etl import extract_posts

def reddit_pipeline(file_name:str, subreddit:str, time_fiter:'day', limit=None):
    #connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airsholar Agent')
    #extraction
    posts= extract_posts(instance, subreddit, time_fiter, limit)
    #transformation
    #loading to csv
