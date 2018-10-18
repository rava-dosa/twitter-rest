## Twitter Search API 

### Description of branches:
1. Added twitter streaming
2. Added PyMongo.
3. Added getting results in .csv.

### Dependencies:-
1. Python 3.6.6
2. Flask 1.0.2
3. TwitterSearch 1.0.2 

### How to run
0. Add secret key and all that in search.py
1. python main.py
2. Click on links to see results.

### Known BUGS
1. I know that ID should be primary key but now due to time constraint I have removed that get results properly even though they are repeated and duplicate.
2. I could have cached **lis** variable for pagination request but again due to time constraint, I have not done that.

### API 1

#### To trigger a twitter search/stream for recent high traffic events.(eg: modi, AbkiBarModiSarkar, ModiForPM etc were high traffic terms during elections back in 2014)
How to use it ?

1. http://127.0.0.1:5000/?keyword=["modi","AbkiBarModiSarkar","ModiForPM"]. This will iterate over all keywords and save top 10 results.
2. http://127.0.0.1:5000/?keyword=["modi","AbkiBarModiSarkar"]&number=20. This will iterate over all keywords and save top 20 result if it's there.

### API 2

#### Flight rules for different usecases.

1. Search tweet
	1. http://127.0.0.1:5000/search?keyword=modi
	2. By default it will search in tweet or if flag=0
2. Search username.
	1. http://127.0.0.1:5000/search?keyword=modi&flag=1
3. Sort by date time.
	1. http://127.0.0.1:5000/search?keyword=modi&sortby=0
4. Sort by tweet text.
	1. http://127.0.0.1:5000/search?keyword=modi&sortby=1
5. Pagination with default capacity 5. Pagination=2 represents second page
	1. http://127.0.0.1:5000/search?keyword=modi&pagination=2
6. Pagination with custom capacity
	1. http://127.0.0.1:5000/search?keyword=modi&pagination=2&capacity=4
7. Filter for date less than a particular date.
	1. http://127.0.0.1:5000/search?keyword=Modi&flag=0&sortby=0&filter=[{'lt':'2018-10-15','var1':'DATE'}]
8. Filter for date which is in range between particular date. There are total three option **lt** for less than **gt** for greater than and **et** for equal to. Options for var1 are **FOLLOWERS**, **FAVOURITES**(Total favourite till date on all tweet), **RETWEET**, **FAVOURITE**(on just this tweet) and **DATE**.
	1. http://127.0.0.1:5000/search?keyword=Modi&flag=0&sortby=0&filter=[{'lt':'2018-10-15','var1':'DATE'},{'gt':'2018-10-05','var1':'DATE'}]
9. Filter for **sw** (Starts with),**ew** (ends with), **contains**(substring search), **exact** (exact match in case of string) . Options for var2 are **ID** (for url search https://twitter.com/i/web/status/ + id) **TWEET** , **USER** for user-id, **NAME** for original name.
	1. http://127.0.0.1:5000/search?keyword=Modi&flag=0&sortby=0&filter=[{'et':'2018-10-15','var1':'DATE'},{'contains':'Modi','var2':'TWEET'}]
10.  You can add as many filter as you want in form of dict. And filter is list of dict. Even though it's not good from security point of view but it decrease no of variables. 
