#name = input('Enter file:')
def removekey(d, key):
    r = dict(d)
    del r[key]
    return r
def entries_to_remove(entries, the_dict):
    for key in entries:
        if key in the_dict:
            del the_dict[key]

from collections import Counter
#name = r"C:\Users\Victor Deng\Desktop\word.txt"
name = r"C:\Users\Victor Deng\Desktop\DataScience\Dreamdata --UCSC\Raw txt\Arlie a middle-aged woman.txt"
handle = open(name, 'r')
counts = dict()
total=0
for line in handle:
    words = line.split()
    for word in words:
        total+=1
        word = word.lower()
        counts[word] = counts.get(word, 0) + 1
entries = ('move', 'and', 'her','the','a','to','of','-','in',"i'm",'it','but','is','on','with','that','my','at','this','or','not','for','get','these','go','some','be','up','like','have',"it's","have","just","there's","are","me,","out","don't","all","as","something","there","back","see","about","so","know","they","very","think","one","do","he's","going","can","if","where","we're","other","what","sort","people","was","an","from","words)","i've","they're","has","been","into","look","them","you","down","arounnd","him","got","come","here","then","maybe","she's","it","by","it,","place","want","now","really","way","when","how","another","looking","right","over","off","here,","around","it.","things","can't","more","kind","here,","through","doesn't","looks","because","lot","quite","big","that's","bit","getting","who","somebody","says","next","which","rather","even","take","comes","me,","front","find","still","sure","while","actually","being","say","after","no","time","also","doing","than","us","these","put","any","i'll","i'd","outside","though","seems","tell","else","start","something,","thing","coming","had","long","pretty","me.","much","keep","away","part","didn't","talking","may","only","too","open","trying","left","would","isn't","we've","turn","cou;d","real","were","make","before","there","here.","thinking","side","shou;d","their","might","work","him,","up","across","could","there,","someone","up,","least","seem","need","who's","inside","first","anything","stop","supposed","along","them,","try","will","ask","building","should","somewhere","having","behind","others","goes","group","end","room,","(i'","call","2","whole","now,","feel","on,","haven't","is,","does","there.","gone","out.","large","few","(i","(or","stuff","sit","that","won't","probably","him.","them.","her.","place,","lots","up.","decide","gets","must","in,","am","small","old","something.","well,","that,","little","his","out,","remember","wall","same","out,","better","guess","on.","why","taking","wants","set","living","live","around,","remember","wall","same","way,","thought","help","well","let","each","without","they've","myself","again","floor","your","new","light","young","gonna","stay","starts","too","used","turns","far","one,","too,","standing","under","pull","near","wearing","again","in.","feeling","hair","what's","ho;d","figure","mostly","leave","this,","again,","hold","that.","since","came","give","close","almost","did","hear","appartment","both","[i","anyway","several","notice","waiting","takes","high","moving","anyway,","people,","last","person","wasn't","dressed","back","different","thing,","show","top","3","though,","enough","outside","say,","seen","pick","round","done","outside,","toward","everybody","its","bit,","already","(the","between","around.","either","drive","our","realize","her,","back.","own","nothing","parking","such","short","nobody","making","gotten","ready","except","two","middle","meant","back,","things,","point","us,","think,","certainly","taken","reason","never","time.","way.","do,","wanted","concerned","now.","too.","finally","says,","down.","use","space","including","off.","together","time,","sound","said,","took","like,","couldn't","turned","knew","gave","dreamt","dream","sudden","called","--","(17))","[laugh]","(16))","somehow","know,","thing.","told","was,","instead","notinon","things.","was,","three","all,","night")
entries_to_remove(entries,counts)
#counts=removegarbage(counts)
d= Counter(counts)
#print(bigword, bigcount)
mostcm=d.most_common()
print (mostcm[:50])
print (total)
