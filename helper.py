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
