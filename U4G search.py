import urllib
import math
import webbrowser
#import Tkinter

###----------------------------------------------------------------------------------------------------------------------------------------
#
##-----------------------------------------------------------------------------------------------------------------------------------------
#GLOBAL USE VARIABLES USED:
#GLOBAL USE VARIABLES GENERATED:
###-----------------------------

ThreadFourURL = "http://mspaforums.com/showthread.php?59466"

ALLPOSTS=[]
RESULTS=[]

###----------------------------------------------------------------------------------------------------------------------------------------
#GET PAGE COUNT FOR THREAD
##-----------------------------------------------------------------------------------------------------------------------------------------
#GLOBAL USE VARIABLES USED:
#ThreadFourURL
#GLOBAL USE VARIABLES GENERATED:
#ThreadFourCount
###-----------------------------

PageOneOf = "Page 1 of "

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

###----------------------------------------------------------------------------------------------------------------------------------------
#GET THE BLOODY POST STRING, PUT IT IN AN ARRAY OF BLOODY POST STRINGS I DONT EVEN CARE ANY MORE
##-----------------------------------------------------------------------------------------------------------------------------------------
#GLOBAL USE VARIABLES USED:
#ThreadFourCount
#ThreadFourURL
#GLOBAL USE VARIABLES GENERATED:
#ALLPOSTS[]
###-----------------------------

##GET POSTS FROM ARCHIVE
page = urllib.urlopen("U4GArchive.html").read().split('<li class="postbitlegacy')
for j in range(0, len(page)):
    ALLPOSTS.append(page[j])
print "ARCHIVE LOADED"

##GET POSTS FROM THREAD FOUR
for i in range(1, ThreadFourCount+1):
    page = urllib.urlopen(ThreadFourURL+"/page"+str(i)).read().split('<li class="postbitlegacy')
    for j in range(1, len(page)):
        ALLPOSTS.append(page[j])
    print "Page %d of %d loaded" % (i,ThreadFourCount)
print "THREAD FOUR LOADED"
print "%d posts counted" % len(ALLPOSTS)
###----------------------------------------------------------------------------------------------------------------------------------------
#GET POST DATA FROM A POST STRING
##-----------------------------------------------------------------------------------------------------------------------------------------
#GLOBAL USE VARIABLES USED:
#GLOBAL USE VARIABLES GENERATED:
#getUser(str POST)
#getPost(str POST)
#getDate(str POST)
#getID(str POST)
###-----------------------------

def getUser(POST):
    return POST.split("strong")[1][1: -2]

def getPost(POST):
    return POST.split('<blockquote class="postcontent restore ">')[1].split('</blockquote>')[0]

def getDate(POST):
    return POST.split('<span class="date">')[1].split(',&nbsp;')[0]

def getID(POST):
	return POST.split('id="post_')[1].split('">')[0]

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
    for i in range(0,len(GETPOSTS)):
        if getUser(GETPOSTS[i]).lower() == USER.lower():
            POSTS.append(GETPOSTS[i])
    return POSTS

def SearchPost(KEYWORDs, ANDOR, GETPOSTS):
    POSTS=[]
    if (" " in KEYWORDs):
        k = KEYWORDs.split()
        if ANDOR:
            inpost = True
            for i in range(0, len(GETPOSTS)):
                for j in range(0, len(k)):
                    if (k[j].lower() in getPost(GETPOSTS[i]).lower()) and inpost:
                        POSTS.append(GETPOSTS[i])
                        inpost = False
                inpost = True
        else:
            kcount = 0
            for i in range(0, len(GETPOSTS)):
                for j in range(0, len(k)):
                    if (k[j].lower() in getPost(GETPOSTS[i]).lower()):
                        kcount += 1
                if kcount == len(k):
                    POSTS.append(GETPOSTS[i])
                kcount = 0
    else:
        for i in range(0, len(GETPOSTS)):
            if(KEYWORDs.lower() in getPost(GETPOSTS[i]).lower()):
                POSTS.append(GETPOSTS[i])
    return POSTS

def SearchDateRange(DATEMIN, DATEMAX, GETPOSTS):
    POSTS=[]
    dmin = DATEMIN.split('-')
    dmax = DATEMAX.split('-')
    for i in range(0,len(GETPOSTS)):
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
#GetID
#RESULTS
#GLOBAL USE VARIABLES GENERATED:
#toHTML
###-----------------------------

def toHTML():
    output = open("SearchResults.html", "w")
    output.write('<html><head><title>GET YOUR U4G SEARCH HERE</title><link rel="stylesheet" href="normalize.css"><link rel="stylesheet" href="css.css"></head><body>')
    for i in range(0, len(RESULTS)):
        output.write('<div class="postdata">')
        output.write("<h2>%s</h2>" % getDate(RESULTS[i]))
        output.write("<h3>%s</h3>" % getID(RESULTS[i]))
        output.write("<h1>%s</h1>" % getUser(RESULTS[i]))
        output.write('<div class="postbody"><p>%s</p></div>' % getPost(RESULTS[i]))
        output.write("</div>")
    output.write("</body></html>")
    output.close()
    webbrowser.open("SearchResults.html", new=2, autoraise=True)

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
        usersearch = raw_input("\nEnter the username to search for.\n")
        if isresults:
            RESULTS = SearchUser(usersearch, ALLPOSTS)
        else:
            RESULTS = SearchUser(usersearch, RESULTS)
        isresults = False
    if searchtype == "2":
        keywordsearch = raw_input("\nEnter a keyword or keywords to search for within the body of the post. Separate keywords with spaces, and avoid punctiation unless that is explicitly a part of your search.\n")
        andorsearch = raw_input("\nSearch by default searches for all keywords. Would you like to instead include results that have any keyword? Type 'YES' if so. ")#True is any, false is all
        andorswitch = False
        if (andorsearch.lower() == "yes"):
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
