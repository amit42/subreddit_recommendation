from flask import Flask , request , render_template

from recommend import *

from pymongo import *

app = Flask(__name__)

client = MongoClient("mongodb+srv://amitkr42:<PASSWORD>@cluster0.kmjih.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

def get_similar_subreddits(subname):
	recommend_sub(subname,client)
	subs = recommend_sub(subname,client)
	names = []
	counts = []
	for sub in subs:
		if sub[0] != subname:
			names.append(sub[0])
			counts.append(sub[1])
	return names,counts
	

@app.route('/')
def home():
    return render_template('base.html')


@app.route('/home', methods=['POST'])
def display():
    subname = request.form.get("similar")
    most_similar = get_similar_subreddits(subname)

    list_string = ""

    names = most_similar[0]
    counts = most_similar[1]
    pairs = zip(names, counts)

    if len(names) == 0:
        list_string = "There was either a misspelling in the subreddit (case-sensitive!), or there is not enough data in /r/" + str(subname) + " to draw a conclusion."
    else:
        list_string = "If you like /r/" + str(subname) + ", you may also enjoy..."

    return render_template('index.html', names=names, counts=counts, subname=list_string, pairs=pairs)


if __name__ == "__main__":
    app.run(debug=True)
