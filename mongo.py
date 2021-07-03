from pymongo import *

def insert_user(username, subreddits , client):
	user = {
			'username' : username,
			'subreddits' : subreddits,
	}
	db = client['reddit']
	collection = db['users']
	collection.update({'username': user['username']}, {'username': user['username'], 'subreddits' : user['subreddits']},upsert = True)


def insert_sub(sub, users, client):
	subreddit = {
		'name' : sub,
		'users' : users
	}
	db = client.reddit
	collection = db.subreddits
	collection.update({'name': subreddit['name']}, {'name':subreddit['name'],'users':subreddit['users']},upsert=True)


