# tweet text, username, dat time, retweet count, favourite count, language, user follower count, user mentions, url.
import search
import sqlite3
import pdb
import time
import model
import helper


from flask import Flask
from flask import json
from flask import request
from werkzeug.contrib.cache import SimpleCache

# import json
from ast import literal_eval
from operator import itemgetter

app = Flask(__name__)
cache = SimpleCache()


@app.route('/')
def hello_world():
	p1=None
	p2=None
	try:
		p1 = request.args.get('keyword')
		p3 = literal_eval(p1)
	except:
		return "hello_world"
	try:
		p2 = request.args.get('number')
	except:
		pass
	for x in p3:
		l2=[x]
		if p2 is not None:
			l1=search.twit(l2,int(p2))
		else:
			l1=search.twit(l2,10)
		ret=model.insert(l1)
	response = app.response_class(
		response=json.dumps(ret),
		status=200,
		mimetype='application/json'
	)
	return response



@app.route('/search')
def summary():
	pdb.set_trace()
	keyforcache=helper.urltokey(request.url)
	time=5*60
	lis=None
	lis=helper.cach(lis,keyforcache,request,cache,time)
	lis=helper.pagination(lis,request)

	# response
	response = app.response_class(
		response=json.dumps(lis),
		status=200,
		mimetype='application/json'
	)
	return response

app.run(debug=True,threaded=True)