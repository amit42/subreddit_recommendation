def query_user(username, client):
	collection = client.reddit.users
	user = collection.find_one({'username':username})
	if user:
		return user['subreddits']
	return get_subreddits(username, client)

def query_subreddit(subreddit, client):
	collection = client.reddit.subreddits
	sub = collection.find_one({'name':subreddit})
	if sub:
		return sub['users']
	return get_users(subreddit, client)

