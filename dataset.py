import praw 
from mongo import *
from pymongo import *


def get_users(subreddit,client):

    result = client.reddit.subreddits.find({'name':subreddit})
    if result.count()>0:
        return result
    reddit = praw.Reddit(client_id ='iDjaNJS3xF7T1A',
                     client_secret ='CZAuHW0uz3p07q09BmYrxcymvuDVBQ',
                     user_agent ='my user agent')
    
    sub = reddit.subreddit(subreddit)
    comments = sub.comments(limit=10)
    users = [i.author.name for i in comments]
    insert_sub(subreddit,users,client)
    return users


def get_subreddits( username , client):
    result = client.reddit.users.find({'username':username})
    if result.count()>0:
        return result
    reddit = praw.Reddit(client_id ='iDjaNJS3xF7T1A',
                            client_secret ='CZAuHW0uz3p07q09BmYrxcymvuDVBQ',
                            user_agent ='my user agent')
    redditor = reddit.redditor(username)
    comments = redditor.comments.new(limit=10)
    subreddits = [i.subreddit.display_name for i in comments]
    insert_user(username , subreddits , client)
    return subreddits


