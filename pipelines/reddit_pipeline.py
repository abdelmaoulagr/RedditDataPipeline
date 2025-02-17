def reddit_pipeline(file_name:str, subreddit:str, time_fiter:'day', limit=None):
    #connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airsholar Agent')
    #extraction
    #transformation
    #loading to csv
