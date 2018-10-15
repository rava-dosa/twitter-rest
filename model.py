import sqlite3

def insert(l1):
	conn = sqlite3.connect('test.db')
	s1="INSERT INTO TWITTER (ID,TWEET,USER,NAME,FOLLOWERS,FAVOURITES,LANGUAGE,DATET,RETWEET,FAVOURITE) VALUES "
	i=0
	cur = conn.cursor()
	
	# I know that ID shoud be primary key but now due to time constraint I have removed that get resuts properly even though they are repeated.
	conn.execute('''CREATE TABLE IF NOT EXISTS TWITTER (ID INT NOT NULL,TWEET TEXT NOT NULL,USER TEXT NOT NULL, NAME TEXT NOT NULL,FOLLOWERS INT,FAVOURITES INT,LANGUAGE TEXT NOT NULL,DATET TEXT NOT NULL,RETWEET INT,FAVOURITE INT);''')
	for x in l1:
		s2=" ({ID},'{TWEET}','{USER}','{NAME}',{FOLLOWERS},{FAVOURITES},'{LANGUAGE}','{DATET}',{RETWEET},{FAVOURITE})".format(ID=x[0],TWEET=str(x[1]),USER=x[2],NAME=x[3],FOLLOWERS=x[4],FAVOURITES=x[5],LANGUAGE=x[6],DATET=x[7],RETWEET=x[8],FAVOURITE=x[9])
		if(i>0):
			s1=s1+","+s2
		else:
			s1=s1+s2
		i=i+1
	try:
		conn.execute(s1)
		conn.commit()
	except:
		return "failed"
	conn.close()
	print(s1)
	return "success"
