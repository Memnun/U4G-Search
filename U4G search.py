import urllib
import Tkinter

###----------------------------------------------------------------------------------------------------------------------------------------
#
##-----------------------------------------------------------------------------------------------------------------------------------------
#GLOBAL USE VARIABLES USED:
#GLOBAL USE VARIABLES GENERATED:
###-----------------------------

ThreadOneURL = "http://mspaforums.com/showthread.php?29535"
ThreadTwoURL = "http://mspaforums.com/showthread.php?55452"
ThreadThreeURL = "http://mspaforums.com/showthread.php?56980"
ThreadFourURL = "http://mspaforums.com/showthread.php?59466"

ALLPOSTS=[]
RESULTS=[]

###----------------------------------------------------------------------------------------------------------------------------------------
#GET PAGE COUNT FOR EACH THREAD
##-----------------------------------------------------------------------------------------------------------------------------------------
#GLOBAL USE VARIABLES USED:
#PageOneOf
#ThreadOneURL
#ThreadTwoURL
#ThreadThreeURL
#ThreadFourURL
#GLOBAL USE VARIABLES GENERATED:
#ThreadOneCount
#ThreadTwoCount
#ThreadThreeCount
#ThreadFourCount
###-----------------------------

PageOneOf = "Page 1 of "

##THREAD 1 GET PAGE COUNT

ThreadOnePageOneHTM = urllib.urlopen(ThreadOneURL).read()
WhereInPage = ThreadOnePageOneHTM.find(PageOneOf)

CountDigitOne = ThreadOnePageOneHTM[WhereInPage + 10]
CountDigitTwo = ThreadOnePageOneHTM[WhereInPage + 11]
CountDigitThr = ThreadOnePageOneHTM[WhereInPage + 12]

if CountDigitThr == '/':
    ThreadOneCount = int(CountDigitOne)
elif CountDigitThr == '<':
    ThreadOneCount = (int(CountDigitOne)*10)+int(CountDigitTwo)
else:
    ThreadOneCount = (int(CountDigitOne)*100)+(int(CountDigitTwo)*10)+int(CountDigitThr)

##THREAD 2 GET PAGE COUNT

ThreadTwoPageOneHTM = urllib.urlopen(ThreadTwoURL).read()
WhereInPage = ThreadTwoPageOneHTM.find(PageOneOf)

CountDigitOne = ThreadTwoPageOneHTM[WhereInPage + 10]
CountDigitTwo = ThreadTwoPageOneHTM[WhereInPage + 11]
CountDigitThr = ThreadTwoPageOneHTM[WhereInPage + 12]

if CountDigitThr == '/':
    ThreadTwoCount = int(CountDigitOne)
elif CountDigitThr == '<':
    ThreadTwoCount = (int(CountDigitOne)*10)+int(CountDigitTwo)
else:
    ThreadTwoCount = (int(CountDigitOne)*100)+(int(CountDigitTwo)*10)+int(CountDigitThr)

##THREAD 3 GET PAGE COUNT

ThreadThreePageOneHTM = urllib.urlopen(ThreadThreeURL).read()
WhereInPage = ThreadThreePageOneHTM.find(PageOneOf)

CountDigitOne = ThreadThreePageOneHTM[WhereInPage + 10]
CountDigitTwo = ThreadThreePageOneHTM[WhereInPage + 11]
CountDigitThr = ThreadThreePageOneHTM[WhereInPage + 12]

if CountDigitThr == '/':
    ThreadThreeCount = int(CountDigitOne)
elif CountDigitThr == '<':
    ThreadThreeCount = (int(CountDigitOne)*10)+int(CountDigitTwo)
else:
    ThreadThreeCount = (int(CountDigitOne)*100)+(int(CountDigitTwo)*10)+int(CountDigitThr)

##THREAD 4 GET PAGE COUNT

ThreadFourPageOneHTM = urllib.urlopen(ThreadFourURL).read()
WhereInPage = ThreadFourPageOneHTM.find(PageOneOf)

CountDigitOne = ThreadFourPageOneHTM[WhereInPage + 10]
CountDigitTwo = ThreadFourPageOneHTM[WhereInPage + 11]
CountDigitThr = ThreadFourPageOneHTM[WhereInPage + 12]

if CountDigitThr == '/':
    ThreadFourCount = int(CountDigitOne)
elif CountDigitThr == '<':
    ThreadFourCount = (int(CountDigitOne)*10)+int(CountDigitTwo)
else:
    ThreadFourCount = (int(CountDigitOne)*100)+(int(CountDigitTwo)*10)+int(CountDigitThr)

print "Thread One Page Count: ", ThreadOneCount
print "Thread Two Page Count: ", ThreadTwoCount
print "Thread Three Page Count: ", ThreadThreeCount
print "Thread Four Page Count: ", ThreadFourCount

###----------------------------------------------------------------------------------------------------------------------------------------
#GET THE BLOODY POST STRING, PUT IT IN AN ARRAY OF BLOODY POST STRINGS I DONT EVEN CARE ANY MORE
##-----------------------------------------------------------------------------------------------------------------------------------------
#GLOBAL USE VARIABLES USED:
#ThreadOneCount
#ThreadTwoCount
#ThreadThreeCount
#ThreadFourCount
#ThreadOneURL
#ThreadTwoURL
#ThreadThreeURL
#ThreadFourURL
#GLOBAL USE VARIABLES GENERATED:
#ALLPOSTS[]
###-----------------------------

##GET POSTS FROM THREAD ONE
for i in range(1, ThreadOneCount):
    page = urllib.urlopen(ThreadOneURL+"/page"+str(i)).read().split('<li class="postbitlegacy')
    for j in range(1, len(page)):
        ALLPOSTS.append(page[j])
    print len(ALLPOSTS)
print "THREAD ONE ARCHIVED"

##GET POSTS FROM THREAD TWO
for i in range(1, ThreadTwoCount):
    page = urllib.urlopen(ThreadTwoURL+"/page"+str(i)).read().split('<li class="postbitlegacy')
    for j in range(1, len(page)):
        ALLPOSTS.append(page[j])
    print len(ALLPOSTS)
print "THREAD TWO ARCHIVED"

##GET POSTS FROM THREAD THREE
for i in range(1, ThreadThreeCount):
    page = urllib.urlopen(ThreadThreeURL+"/page"+str(i)).read().split('<li class="postbitlegacy')
    for j in range(1, len(page)):
        ALLPOSTS.append(page[j])
    print len(ALLPOSTS)
print "THREAD THREE ARCHIVED"

##GET POSTS FROM THREAD FOUR
for i in range(1, ThreadFourCount):
    page = urllib.urlopen(ThreadFourURL+"/page"+str(i)).read().split('<li class="postbitlegacy')
    for j in range(1, len(page)):
        ALLPOSTS.append(page[j])
    print len(ALLPOSTS)
print "THREAD FOUR ARCHIVED"

###----------------------------------------------------------------------------------------------------------------------------------------
#GET POST DATA FROM A POST STRING
##-----------------------------------------------------------------------------------------------------------------------------------------
#GLOBAL USE VARIABLES USED:
#GLOBAL USE VARIABLES GENERATED:
#getUser(str POST)
#getPost(str POST)
#getDate(str POST)
###-----------------------------

def getUser(POST):
    return POST.split("strong")[1][1: -2]

def getPost(POST):
    return POST.split('<blockquote class="postcontent restore ">')[1].split('</blockquote>')[0]

def getDate(POST):
    return POST.split('<span class="date">')[1].split(',&nbsp;')[0]

###----------------------------------------------------------------------------------------------------------------------------------------
#SEARCH FUNCTIONS
##-----------------------------------------------------------------------------------------------------------------------------------------
#GLOBAL USE VARIABLES USED:
#ALLPOSTS
#GLOBAL USE VARIABLES GENERATED:
#SearchUser(str USER, GETPOSTS)[]
#SearchPost(str KEYWORDs, ANDOR, GETPOSTS)[] True is OR, False is AND
#SearchDateRange(str DATE-MIN, str DATE-MAX, GETPOSTS)[] dates formatted MM-DD-YYYY
###-----------------------------

def SearchUser(USER, GETPOSTS):
    POSTS=[]
    for i in range(0,len(GETPOSTS)-1):
        if getUser(GETPOSTS[i]) == USER:
            POSTS.append(GETPOSTS[i])
    return POSTS

def SearchPost(KEYWORDs, ANDOR, GETPOSTS):
	POSTS=[]
	if (" " in KEYWORDs):
		k = KEYWORDs.split()
		if ANDOR:
			inpost = True
			for i in range(0, len(GETPOSTS)-1):
				for j in range(0, len(k)-1):
					if (k[j].lower() in getPost(GETPOSTS[i]).lower()) and inpost:
						POSTS.append(GETPOSTS[i])
						inpost = False
				inpost = True
		else:
			kcount = 0
			for i in range(0, len(GETPOSTS)-1):
				for j in range(0, len(k)-1):
					if (k[j].lower() in getPost(GETPOSTS[i]).lower()):
						kcount += 1
				if kcount == len(k):
					POSTS.append(GETPOSTS[i])
				kcount = 0
	else:
		for i in range(0, len(GETPOSTS)-1):
			if(KEYWORDs.lower() in getPost(GETPOSTS[i]).lower()):
				POSTS.append(GETPOSTS[i])
	return POSTS

def SearchDateRange(DATEMIN, DATEMAX, GETPOSTS):
    POSTS=[]
    dmin = DATEMIN.split('-')
    dmax = DATEMAX.split('-')
    for i in range(0,len(GETPOSTS)-1):
        pdate = getDate(GETPOSTS[i]).split('-')
        Greater = False
        Less = False
        if int(pdate[2]) > int(dmin[2]):
            Greater = True
        elif int(pdate[2]) == int(dmin[2]):
            if int(pdate[0]) > int(dmin[0]):
                Greater = True
            elif int(pdate[0]) == int(dmin[0]):
                if int(pdate[1]) >= int(dmin[1]):
                    Greater = True
        if int(pdate[2]) < int(dmax[2]):
            Less = True
        elif int(pdate[2]) == int(dmax[2]):
            if int(pdate[0]) < int(dmax[0]):
                Less = True
            elif int(pdate[0]) == int(dmax[0]):
                if int(pdate[1]) <= int(dmax[1]):
                    Less = True
        if Greater == True and Less == True:
            POSTS.append(GETPOSTS[i])
    return POSTS

###----------------------------------------------------------------------------------------------------------------------------------------
#WRITING SEARCH RESULTS TO AN HTML DOCUMENT
##-----------------------------------------------------------------------------------------------------------------------------------------
#GLOBAL USE VARIABLES USED:
#GetUser
#GetPost
#GetDate
#RESULTS
#GLOBAL USE VARIABLES GENERATED:
###-----------------------------

def toHTML():
    output = open("SearchResults.html", "w")
    output.write("<html><head><title>GET YOUR U4G SEARCH HERE</title></head><body>")
    for i in range(0, len(RESULTS)-1):
        output.write("<h2>%s</h2>" % getDate(RESULTS[i]))
        output.write("<h1>%s</h1>" % getUser(RESULTS[i]))
        output.write("<p>%s</p>" % getPost(RESULTS[i]))
    output.write("</body></html>")
    output.close()

###----------------------------------------------------------------------------------------------------------------------------------------
#SEARCH PROCESSING IS DONE HERE -----------------------------------------------------------------------------------------------------------CURRENTLY BROKEN, DO NOT UNCOMMENT
##-----------------------------------------------------------------------------------------------------------------------------------------
#GLOBAL USE VARIABLES USED:
#ALLPOSTS
#SearchUser
#SearchPost
#SearchDateRange
#GLOBAL USE VARIABLES GENERATED:
#RESULTS
###-----------------------------
"""
looping = True

class searchengine(Tkinter.Tk):
    def __init__(self, parent):
        self.initialize()

    def initialize(self):
        #self.grid()

        SearchByUser = Tkinter.Button(self, text = u"Search Users", command = self.onUser)

        SearchByKeywordsAND = Tkinter.Button(self, text = u"Search by Keyword(s), match all", command = self.onKeywordsAND)

        SearchByKeywordsOR = Tkinter.Button(self, text = u"Search by Keyword(s), match any", command = self.onKeywordsOR)

        SearchByDate = Tkinter.Button(self, text = u"Search by Date Range", command = self.onDates)

        self.userentry = Tkinter.StringVar()
        UserEntry = Tkinter.Entry(self, textvariable = self.userentry, anchor = 'w')

        self.keywordentry = Tkinter.StringVar()
        KeywordEntry = Tkinter.Entry(self, textvariable = self.keywordentry, anchor = 'w')

        self.dateminentry = Tkinter.StringVar()
        DateMinEntry = Tkinter.Entry(self, textvariable = self.dateminentry, anchor = 'w')

        self.datemaxentry = Tkinter.StringVar()
        DateMaxEntry = Tkinter.Entry(self, textvariable = self.datemaxentry, anchor = 'w')

        userlabel = Tkinter.Label(self, anchor = 'w')
        userlabel.set("Username: (Capitalization counts)")

        keywordlabel = Tkinter.Label(self, anchor = 'w')
        keywordlabel.set("Keywords: (capitalization counts, please don't add punctuation)")

        dateminlabel = Tkinter.Label(self, anchor = 'w')
        dateminlabel.set("Date Min: (MM-DD-YYYY)")

        datemaxlabel = Tkinter.Label(self, anchor = 'w')
        datemaxlabel.set("Date Max: (MM-DD-YYYY)")

        printout = Tkinter.Button(self, text = u"Get Search Results", command = self.onout)

        SearchByUser.grid(column = 2, row = 0, rowspan = 2)

        SearchByKeywordsAND.grid(column = 2, row = 2, rowspan = 2)

        SearchByKeywordsOR.grid(column = 3, row = 2, rowspan = 2)

        SearchByDate.grid(column = 2, row = 4, rowspan = 2)

        UserEntry.grid(column = 0, row = 1, columnspan = 2, sticky = 'EW')

        KeywordEntry.grid(column = 0, row = 3, sticky = 'EW')

        DateMinEntry.grid(column = 0, row = 5, sticky = 'EW')

        DateMaxEntry.grid(column = 1, row = 5, sticky = 'EW')

        userlabel.grid(column = 0, row = 0, columnspan = 2, sticky = 'EW')

        keywordlabel.grid(column = 0, row = 2, columnspan = 2, sticky = 'EW')

        dateminlabel.grid(column = 0, row = 4, sticky = 'EW')

        datemaxlabel.grid(column = 1, row = 4, sticky = 'EW')

        printout.grid(column = 0, row = 6, columnspan = 4)

    def onUser(self):
        if getUser(RESULTS[0]) != True:
            RESULTS = SearchByUser(self.userentry.get(), ALLPOSTS)
        else:
            RESULTS = SearchByUser(self.userentry.get(), RESULTS)

    def onKeywordsAND(self):
        if getUser(RESULTS[0]) != True:
            RESULTS = SearchByKeywords(self.keywordentry.get(), False, ALLPOSTS)
        else:
            RESULTS = SearchByKeywords(self.keywordentry.get(), False, RESULTS)

    def onKeywordsOR(self):
        if getUser(RESULTS[0]) != True:
            RESULTS = SearchByKeywords(self.keywordentry.get(), True, ALLPOSTS)
        else:
            RESULTS = SearchByKeywords(self.keywordentry.get(), True, RESULTS)

    def onDates(self):
        if getUser(RESULTS[0]) != True:
            RESULTS = SearchByKeywords(self.keywordentry.get(), ALLPOSTS)
        else:
            RESULTS = SearchByKeywords(self.keywordentry.get(), RESULTS)

    def onout(self):
        toHTML()
        looping = False

if __name__ == "__main__":
    app = searchengine(None)
    app.title('U4G Search Engine')
    while looping:
        app.mainloop()
"""

###----------------------------------------------------------------------------------------------------------------------------------------
#TEXT BASED FRONT END
##-----------------------------------------------------------------------------------------------------------------------------------------
#GLOBAL USE VARIABLES USED:
#getUser
#SearchUser
#SearchPost
#SearchDateRange
#toHTML
#ALLPOSTS
#RESULTS
#GLOBAL USE VARIABLES GENERATED:
###-----------------------------

isresults = True
while True:
	searchtype = raw_input("\nSelect a search method; type 1 for Username, 2 for keyword(s), or 3 for a date range. Alternatively, type 4 to get your search results or 5 to reset search criteria ")
	if searchtype == "1":
		usersearch = raw_input("\nEnter the username to search for. Remember, capitalization matters!\n")
		if isresults:
			RESULTS = SearchUser(usersearch, ALLPOSTS)
		else:
			RESULTS = SearchUser(usersearch, RESULTS)
		isresults = False
	if searchtype == "2":
		keywordsearch = raw_input("\nEnter a keyword or keywords to search for within the body of the post. Separate keywords with spaces, and avoid punctiation unless that is explicitly a part of your search.\n")
		andorsearch = raw_input("\nSearch by default searches for all keywords. Would you like to instead include results that have any keyword? Type 'YES' if so. ")#True is any, false is all
		andorswitch = False
		if (andorsearch == "YES"):
			andorswitch = True
		if isresults:
			RESULTS = SearchPost(keywordsearch, andorswitch, ALLPOSTS)
		else:
			RESULTS = SearchPost(keywordsearch, andorswitch, RESULTS)
		isresults = False
	if searchtype == "3":
		dateminsearch = raw_input("\nEnter the minimum date; any posts older than this will be excluded from your search. Format as MM-DD-YYYY\n")
		datemaxsearch = raw_input("\nEnter the maximum date; any posts newer than this will be excluded from your search. Format as MM-DD-YYYY\n")
		if isresults:
			RESULTS = SearchDateRange(dateminsearch, datemaxsearch, ALLPOSTS)
		else:
			RESULTS = SearchDateRange(dateminsearch, datemaxsearch, RESULTS)
		isresults = False
	if searchtype == "4" and isresults == False:
		toHTML()
	if searchtype == "5":
		isresults = True
		print "\nSearch criteria reset."