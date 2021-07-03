
from query import *

def update_freq( freq , subreddits):
	for subreddit in subreddits:
		if subreddit in freq:
			freq[subreddit] = freq[subreddit]+1
		else:
			freq[subreddit] = 1


def get_freq(subreddit , client):
	users = query_subreddit(subreddit , client)
	freq = {}
	for user in users :
		subreddits = query_user(user , client)
		update_freq(freq , subreddits)
	return freq

def recommend_sub(subreddit , client):
	freq = get_freq(subreddit , client)
	ret = []
	for sub in sorted( freq , key = freq.get , reverse = True):
		ret.append((sub,freq[sub]))
	return ret

