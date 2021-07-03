from pymongo import *

def insert_user(username, subreddits , client):
	user = {
			'username' : username,
			'subreddits' : subreddits,
	}
	db = client['reddit']
	collection = db['users']
	collection.update({'username': user['username']}, {'username': user['username'], 'subreddits' : user['subreddits']},upsert = True)

def insert_sub(sub, client):

	db = client.reddit
	collection = db.subreddits
	collection.update({'name': sub}, {'name':sub},upsert=True)
"""
def query_user(username, client):
	collection = client.reddit.users
	user = collection.find_one({'username':username})
	return user

def subreddits(client):
	return client.reddit.subreddits.find()

def multiple_users(user_array, client):
	return client.reddit.users.find({'username' : {"$in":user_array}})

def temp_users(client):
	return client.reddit.temp.find()

def all_users(client):
	return client.reddit.users.find()

def temp_insert(users,client):
	client.reddit.temp.insert(users)
"""