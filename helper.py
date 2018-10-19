import re
import model
# import 
def main1(lis,request):
	p1=None
	p11=None
	p3=None
	p4=None
	p5=None
	p6=None
	try:
		p1 = request.args.get('keyword')
	except:
		pass
	try:
		p11 = request.args.get('sortby')
	except:
		pass
		#p11 = 0 sort by date time
		#p11 = 1 sort by tweet text.
	try:	
		p3 = request.args.get('flag')       
	except:
		pass	
		# flag = 0 if search keyword is for tweet
		# flag = 1 if search keyword is for username 
		# default tweet text
	try:
		p4 = request.args.get('filter')
		if p4 is not None:
			p5 = literal_eval(p4)
		else:
			pass
	except:
		pass
	try:
		p6 = request.args.get('file')
	except:
		pass

	if p1 is not None:
		if p3 is None or int(p3)==0:
			lis=model.searchtweet(lis,p1)
		else:
			lis=model.searchuser(lis,p1)
		# sort by 
		if p11 is not None:
			if int(p11)==0:
				lis=sorted(lis, key=itemgetter(1))
			else:
				lis=sorted(lis, key=itemgetter(7))
		else:
			pass
		# all these(112-144) variables help in producing filter over the queried result
		if p4 is not None:
			var1,var2 = None,None
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
				if var1 is not None:
					if "lt" in x:
						lis=funcoo(lis,x["lt"],var1,0)
					elif "gt" in x:
						lis=funcoo(lis,x["gt"],var1,1)
					elif "et" in x:
						lis=funcoo(lis,x["et"],var1,2)
					else:
						pass

				if var2 is not None:
					if "sw" in x:
						lis=funcoo1(lis,x["sw"],var2,0)
					elif "ew" in x:
						lis=funcoo1(lis,x["ew"],var2,1)
					elif "contains" in x:
						lis=funcoo1(lis,x["contains"],var2,2)
					elif "exact" in x:
						lis=funcoo1(lis,x["exact"],var2,3)
					else:
						pass
	return lis

def f0(lis,lis1,index,val):
	for x in lis:
		if x[index]<val:
			lis1.append(x)
		else:
			pass
	return lis1

def f1(lis,lis1,index,val):
	for x in lis:
		if x[index]>val:
			lis1.append(x)
		else:
			pass
	return lis1

def f2(lis,lis1,index,val):
	for x in lis:
		if x[index]==val:
			lis1.append(x)
		else:
			pass
	return lis1


def funcoo(lis,val,var1,flag):
	lis1=[]
	if flag==0:
		if var1=="FOLLOWERS":
			lis1=f0(lis,lis1,4,val)

		elif var1=="FAVOURITES":
			lis1=f0(lis,lis1,5,val)


		elif var1=="RETWEET":
			lis1=f0(lis,lis1,8,val)

		elif var1=="FAVOURITE":
			lis1=f0(lis,lis1,9,val)

		elif var1=="DATE":
			lis1=f0(lis,lis1,7,val)

	elif flag==1:
		if var1=="FOLLOWERS":
			lis1=f1(lis,lis1,4,val)

		elif var1=="FAVOURITES":
			lis1=f1(lis,lis1,5,val)


		elif var1=="RETWEET":
			lis1=f1(lis,lis1,8,val)

		elif var1=="FAVOURITE":
			lis1=f1(lis,lis1,9,val)

		elif var1=="DATE":
			lis1=f1(lis,lis1,7,val)

	elif flag==2:
		if var1=="FOLLOWERS":
			lis1=f2(lis,lis1,4,val)


		elif var1=="FAVOURITES":
			lis1=f1(lis,lis1,5,val)


		elif var1=="RETWEET":
			lis1=f1(lis,lis1,8,val)

		elif var1=="FAVOURITE":
			lis1=f1(lis,lis1,9,val)

		elif var1=="DATE":
			for x in lis:
				if x[7].split(" ")[0]==val:
					lis1.append(x)
				else:
					pass
	return lis1



def f10(lis,lis1,index,val):
	for x in lis:
		if str(x[index]).startswith(val):
			lis1.append(x)
	return lis1

def f11(lis,lis1,index,val):
	for x in lis:
		if str(x[index]).endswith(val):
			lis1.append(x)
	return lis1

def f12(lis,lis1,index,val):
	for x in lis:
		if val in x[index]:
			lis1.append(x)

	return lis1
def f13(lis,lis1,index,val):
	for x in lis:
		if x[index]==val:
			lis1.append(x)
		else:
			pass
	return lis1




def funcoo1(lis,val,var2,flag):
	lis1=[]
	if flag==0:
		if var2=="ID":
			for x in lis:
				if str(x[0]).startswith(val):
					lis1.append(x)
		elif var2=="TWEET":
			lis1=f10(lis,lis1,1,val)

		elif var2=="USER":
			lis1=f10(lis,lis1,2,val)
		elif var2=="NAME":
			lis1=f10(lis,lis1,3,val)


	if flag==1:
		if var2=="ID":
			for x in lis:
				if str(x[0]).endswith(val):
					lis1.append(x)

		elif var2=="TWEET":
			lis1=f11(lis,lis1,1,val)

		elif var2=="USER":
			lis1=f10(lis,lis1,2,val)
		elif var2=="NAME":
			lis1=f10(lis,lis1,3,val)

	if flag==2:
		if var2=="ID":
			for x in lis:
				if val in str(x[0]):
					lis1.append(x)

		elif var2=="TWEET":
			lis1=f12(lis,lis1,1,val)


		elif var2=="USER":
			lis1=f12(lis,lis1,2,val)

		elif var2=="NAME":
			lis1=f12(lis,lis1,3,val)

	if flag==3:
		if var2=="ID":
			for x in lis:
				if val == str(x[0]):
					lis1.append(x)

		elif var2=="TWEET":
			lis1=f13(lis,lis1,1,val)

		elif var2=="USER":
			lis1=f13(lis,lis1,2,val)

		elif var2=="NAME":
			lis1=f13(lis,lis1,3,val)

	return lis1

def urltokey(str1):
	# I know that key can be better. Like we can sequentialize filter options to create a key. 
	try:
		str1=re.sub('&pagination=\d+', '', str1)
	except:
		pass
	try:
		str1=re.sub('&capacity=\d+', '', str1)
	except:
		pass
	return str1

def pagination(lis,request):
	p2=None
	p22=None
	try:
		# pdb.set_trace()
		p2 = request.args.get('pagination')
	except:
		pass

	try:	
		p22 = request.args.get('capacity')
	except:
		pass

	# pagination 
	if p2 is not None:
		if p22 is not None:
			# pdb.set_trace()
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
		else:
			cap=5
			pag=int(p2)
			currcap=len(lis)-pag*cap
			if pag*cap < len(lis):
				if currcap > cap:
					lis=lis[pag*cap:pag*cap+cap]
				else:
					lis=lis[pag*cap:len(lis)]
			else:
				return("Bad request")

	return lis

def cach(lis,keyforcache,request,cache,time):
	lis = cache.get(keyforcache)
	if lis is None:
		lis=[]
		lis = main1(lis,request)
		cache.set(keyforcache, lis, timeout=time)
	return lis