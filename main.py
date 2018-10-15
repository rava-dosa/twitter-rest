# tweet text, username, dat time, retweet count, favourite count, language, user follower count, user mentions, url.
import search
import sqlite3
import pdb
import time
import model
import helper
import streaming

from flask import Flask
from flask import json
from flask import request
# import json
from ast import literal_eval
from operator import itemgetter

app = Flask(__name__)

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
			# l1=search.twit(l2,int(p2))
			l1=streaming.twit(l2,int(p2))
		else:
			# l1=search.twit(l2,10)
			l1=streaming.twit(l2,10)
		ret=model.insert(l1)
	response = app.response_class(
		response=json.dumps(ret),
		status=200,
		mimetype='application/json'
	)
	return response

@app.route('/search')
def summary():
	data = {'a':100,'b':200}
	conn = sqlite3.connect('test.db')
	lis=[]
	p1=None
	p11=None
	p2=None
	p22=None
	p3=None
	p4=None
	p5=None
	try:
		p1 = request.args.get('keyword')
		p11 = request.args.get('sortby')
		#p11 = 0 sort by date time
		#p11 = 1 sort by tweet text.
		p2 = request.args.get('pagination')
		p22 = request.args.get('capacity')
		p3 = request.args.get('flag')       
		# flag = 0 if search keyword is for tweet
		# flag = 1 if search keyword is for username 
		# default tweet text
		p4 = request.args.get('filter')
		if p4 is not None:
			p5 = literal_eval(p4)
		else:
			pass
	except:
		pass
	if p1 is not None:
		if p3 is None or int(p3)==0:
			s1="SELECT * FROM TWITTER WHERE TWEET LIKE '%{keyword}%' ".format(keyword=p1)
			print(s1)
			for row in conn.execute(s1):
				# print(row)
				lis.append(row)
		else:
			s1="SELECT * FROM TWITTER WHERE USER LIKE '%{keyword}%' ".format(keyword=p1)
			print(s1)
			for row in conn.execute(s1):
				# print(row)
				lis.append(row)
		if p11 is not None:
			if int(p11)==0:
				lis=sorted(lis, key=itemgetter(1))
			else:
				lis=sorted(lis, key=itemgetter(7))
		else:
			pass
		if p4 is not None:
			for x in p5:
				try:
					var1 = x["var1"]
				except:
					pass
				try:
					var2 = x["var2"]
				except:
					pass
				# pdb.set_trace()
				if "lt" in x:
					lis=helper.funcoo(lis,x["lt"],var1,0)
				elif "gt" in x:
					lis=helper.funcoo(lis,x["gt"],var1,1)
				elif "et" in x:
					lis=helper.funcoo(lis,x["et"],var1,2)
				else:
					pass

				if "sw" in x:
					lis=helper.funcoo1(lis,x["sw"],var2,0)
				elif "ew" in x:
					lis=helper.funcoo1(lis,x["ew"],var2,1)
				elif "contains" in x:
					lis=helper.funcoo1(lis,x["contains"],var2,2)
				elif "exact" in x:
					lis=helper.funcoo1(lis,x["exact"],var2,3)
				else:
					pass
	if p2 is not None:
		if p22 is not None:
			pag=int(p2)
			cap=int(p22)
			currcap=len(lis)-pag*cap
			if pag*cap < len(lis):
				if currcap > cap:
					lis=lis[pag*cap:pag*cap+cap]
				else:
					lis=lis[pag*cap:len(lis)]
			else:
				return("Bad request")
	response = app.response_class(
		response=json.dumps(lis),
		status=200,
		mimetype='application/json'
	)
	return response

app.run(debug=True,threaded=True)