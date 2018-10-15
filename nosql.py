import pymongo
import pdb
def insert(l1):
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	mydb = myclient["database"]
	mycol = mydb["TWITTER"]
	mylist = []
	for x in l1:
		dic={}
		dic["ID"]=x[0]
		dic["TWEET"]=x[1]
		dic["USER"]=x[2]
		dic["NAME"]=x[3]
		dic["FOLLOWERS"]=x[4]
		dic["FAVOURITES"]=x[5]
		dic["LANGUAGE"]=x[6]
		dic["DATET"]=x[7]
		dic["RETWEET"]=x[8]
		dic["FAVOURITE"]=x[9]
		mylist.append(dic)
	x = mycol.insert_many(mylist)
	print(x.inserted_ids) 
	return "success"

def searchtweet(l,keyword):
	# l=[]
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	mydb = myclient["database"]
	mycol = mydb["TWITTER"]
	s1="{}".format(keyword)
	dic={}
	dic["$regex"]=s1
	dic["$options"]="i"
	mydoc = mycol.find({"TWEET": dic})
	for x in mydoc:
		# pdb.set_trace()
		l1=list(x.values())
		l.append(l1[1:])
	return l

def searchuser(l,keyword):
	# l=[]
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	mydb = myclient["database"]
	mycol = mydb["TWITTER"]
	s1="/{}/".format(keyword)
	mydoc = mycol.find({"USER": s1})
	for x in mydoc:
		l1=list(x.values())
		l.append(l1)
	return l	