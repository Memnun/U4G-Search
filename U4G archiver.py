import urllib

ThreadOneURL = "http://mspaforums.com/showthread.php?29535"
ThreadTwoURL = "http://mspaforums.com/showthread.php?55452"
ThreadThreeURL = "http://mspaforums.com/showthread.php?56980"

ALLPOSTS=[]
RESULTS=[]

###----------------------------------------------------------------------------------------------------------------------------------------
#GET PAGE COUNT FOR EACH THREAD
##-----------------------------------------------------------------------------------------------------------------------------------------
#GLOBAL USE VARIABLES USED:
#ThreadOneURL
#ThreadTwoURL
#ThreadThreeURL
#GLOBAL USE VARIABLES GENERATED:
#ThreadOneCount
#ThreadTwoCount
#ThreadThreeCount
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

print "Thread One Page Count: ", ThreadOneCount
print "Thread Two Page Count: ", ThreadTwoCount
print "Thread Three Page Count: ", ThreadThreeCount

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
for i in range(1, ThreadOneCount+1):
    page = urllib.urlopen(ThreadOneURL+"/page"+str(i)).read().split('<li class="postbitlegacy')
    for j in range(1, len(page)):
        ALLPOSTS.append(page[j])
    print i
print "THREAD ONE ARCHIVED"

##GET POSTS FROM THREAD TWO
for i in range(1, ThreadTwoCount+1):
    page = urllib.urlopen(ThreadTwoURL+"/page"+str(i)).read().split('<li class="postbitlegacy')
    for j in range(1, len(page)):
        ALLPOSTS.append(page[j])
    print i
print "THREAD TWO ARCHIVED"

##GET POSTS FROM THREAD THREE
for i in range(1, ThreadThreeCount+1):
    page = urllib.urlopen(ThreadThreeURL+"/page"+str(i)).read().split('<li class="postbitlegacy')
    for j in range(1, len(page)):
        ALLPOSTS.append(page[j])
    print i
print "THREAD THREE ARCHIVED"

###----------------------------------------------------------------------------------------------------------------------------------------
#PUT THE ARCHIVE IN A FILE LOCALLY
##-----------------------------------------------------------------------------------------------------------------------------------------
#GLOBAL USE VARIABLES USED:
#ALLPOSTS[]
#GLOBAL USE VARIABLES GENERATED:
###-----------------------------

output = open("U4GArchive.html", "w")
for i in range(0, len(ALLPOSTS)):
    output.write(ALLPOSTS[i])
    if i < (len(ALLPOSTS)-1):
        output.write('<li class="postbitlegacy')
output.close()