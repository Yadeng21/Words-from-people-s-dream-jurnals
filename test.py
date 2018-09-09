import pdfkit
path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
#pdfkit.from_url("http://google.com", r"C:\Users\Victor Deng\Desktop\Myreport\out.pdf", configuration=config)

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
import glob
import errno
path="C:/Users/Victor Deng/Desktop/DataScience/Dreamdata --UCSC/Raw txt/*.txt"
files = glob.glob(path)
#print (files)
titles=""
for name in files:
    try:
        handle = open(name, 'r')
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise
    counts = dict()
    total = 0
    #titles+=1
    titles=name.split('/')
    titles=titles[6]
    title=titles.split('\\')
    title=title[1]
    ftitle=title.split('.')
    ftitle=ftitle[0]
    print (ftitle,"has been graphed")
    #print (titles,"has been graphed")
    #title=titles[6]
    for line in handle:
        words = line.split()
        for word in words:
            total += 1
            word = word.lower()
            counts[word] = counts.get(word, 0) + 1
    entries = (
    'move', 'and', 'her', 'the', 'a', 'to', 'of', '-', 'in', "i'm", 'it', 'but', 'is', 'on', 'with', 'that', 'my', 'at',
    'this', 'or', 'not', 'for', 'get', 'these', 'go', 'some', 'be', 'up', 'like', 'have', "it's", "have", "just",
    "there's", "are", "me,", "out", "don't", "all", "as", "something", "there", "back", "see", "about", "so", "know",
    "they", "very", "think", "one", "do", "he's", "going", "can", "if", "where", "we're", "other", "what", "sort",
    "people", "was", "an", "from", "words)", "i've", "they're", "has", "been", "into", "look", "them", "you", "down",
    "arounnd", "him", "got", "come", "here", "then", "maybe", "she's", "it", "by", "it,", "place", "want", "now",
    "really", "way", "when", "how", "another", "looking", "right", "over", "off", "here,", "around", "it.", "things",
    "can't", "more", "kind", "here,", "through", "doesn't", "looks", "because", "lot", "quite", "big", "that's", "bit",
    "getting", "who", "somebody", "says", "next", "which", "rather", "even", "take", "comes", "me,", "front", "find",
    "still", "sure", "while", "actually", "being", "say", "after", "no", "time", "also", "doing", "than", "us", "these",
    "put", "any", "i'll", "i'd", "outside", "though", "seems", "tell", "else", "start", "something,", "thing", "coming",
    "had", "long", "pretty", "me.", "much", "keep", "away", "part", "didn't", "talking", "may", "only", "too", "open",
    "trying", "left", "would", "isn't", "we've", "turn", "cou;d", "real", "were", "make", "before", "there", "here.",
    "thinking", "side", "shou;d", "their", "might", "work", "him,", "up", "across", "could", "there,", "someone", "up,",
    "least", "seem", "need", "who's", "inside", "first", "anything", "stop", "supposed", "along", "them,", "try",
    "will", "ask", "building", "should", "somewhere", "having", "behind", "others", "goes", "group", "end", "room,",
    "(i'", "call", "2", "whole", "now,", "feel", "on,", "haven't", "is,", "does", "there.", "gone", "out.", "large",
    "few", "(i", "(or", "stuff", "sit", "that", "won't", "probably", "him.", "them.", "her.", "place,", "lots", "up.",
    "decide", "gets", "must", "in,", "am", "small", "old", "something.", "well,", "that,", "little", "his", "out,",
    "remember", "wall", "same", "out,", "better", "guess", "on.", "why", "taking", "wants", "set", "living", "live",
    "around,", "remember", "wall", "same", "way,", "thought", "help", "well", "let", "each", "without", "they've",
    "myself", "again", "floor", "your", "new", "light", "young", "gonna", "stay", "starts", "too", "used", "turns",
    "far", "one,", "too,", "standing", "under", "pull", "near", "wearing", "again", "in.", "feeling", "hair", "what's",
    "ho;d", "figure", "mostly", "leave", "this,", "again,", "hold", "that.", "since", "came", "give", "close", "almost",
    "did", "hear", "appartment", "both", "[i", "anyway", "several", "notice", "waiting", "takes", "high", "moving",
    "anyway,", "people,", "last", "person", "wasn't", "dressed", "back", "different", "thing,", "show", "top", "3",
    "though,", "enough", "outside", "say,", "seen", "pick", "round", "done", "outside,", "toward", "everybody", "its",
    "bit,", "already", "(the", "between", "around.", "either", "drive", "our", "realize", "her,", "back.", "own",
    "nothing", "parking", "such", "short", "nobody", "making", "gotten", "ready", "except", "two", "middle", "meant",
    "back,", "things,", "point", "us,", "think,", "certainly", "taken", "reason", "never", "time.", "way.", "do,",
    "wanted", "concerned", "now.", "too.", "finally", "says,", "down.", "use", "space", "including", "off.", "together",
    "time,", "sound", "said,", "took", "like,", "couldn't", "turned", "knew", "gave", "dreamt", "dream", "sudden",
    "called", "--", "(17))", "[laugh]", "(16))", "somehow", "know,", "thing.", "told", "was,", "instead", "notinon",
    "things.", "was,", "three", "all,", "night", "i", "we", "said","me","he","she",'"i','"oh,','"you','"oh','"boss"',"went","(12))","(2003-04-26","(2003-07-16","(2004-01-03","(2003-09-11","(13))","(14))","(15))","(18))","(19))","(25))","(23))","(22))","(24))","(15))","(19))","started","asked","([age","20-21])","14-15])","16])","13])","seemed","suddenly","dreamed","3)","(24","52","(31","(20))","(it","c","h","d","f","&","(1981)","12])","17])","18])",'"well',"(age","15))","14))","first,","somewhere,","dream.","(0668)","(a","hadn't","r.","no,","saw","kept","s","this.","saying","weren't","needed","everyone","yet","(july","1981)","above","wouldn't","they'd","onto","felt","dream.","everyone","held","most","however,","before,","us.","soon","then,","(although","so,","(which","although","tells","seeing","(in","year","away,","dreams","size","onto","4","1980)","...","they'd","until","anything.","did.","years","upon","before.","was.","and,","to,","apparently","one.","able","(and","dream,","all.","away.","(2000/2001","(2001","(1999/2000","(late)","(2000","(early)","(1999","somebody's","off,")
    entries_to_remove(entries, counts)
    # counts=removegarbage(counts)
    d = Counter(counts)
    # print(bigword, bigcount)
    mostcm = d.most_common()
    #print (mostcm[:50])
    print (total)
    x = sorted(counts, key=counts.get, reverse=True)
    highest = None
    lowest = None
    for k in x[:100]:
        if highest is None or highest < counts[k]:
            highest = counts[k]
        if lowest is None or lowest > counts[k]:
            lowest = counts[k]
    print('Range of counts:', highest, lowest)

    # Spread the font sizes across 20-100 based on the count
    bigsize = 80
    smallsize = 20
    titles = str(titles)
    #fhand = open('gword',titles,'.js', 'w')
    fhand = open(ftitle+'.js', 'w')
    fhand.write("gword = [")
    first = True
    for k in x[:100]:
        if not first: fhand.write(",\n")
        first = False
        size = counts[k]
        size = (size - lowest) / float(highest - lowest)
        size = int((size * bigsize) + smallsize)
        fhand.write('{text: "' + k + '", size: ' + str(size) + '}')
    fhand.write("\n];\n")
    #titles=int(titles)
    fhand.close()
    fhand2 = open(ftitle+'.htm','w')
    fhand2.write("""<!DOCTYPE html>
<meta charset="utf-8">
<script src="d3.v2.js"></script>
<script src="d3.layout.cloud.js"></script>""")
    fhand2.write('\n'+'<script src='+'"'+ftitle+'.js'+'"'+'></script>')
    fhand2.write('\n'+'''<body>
<script>
  var fill = d3.scale.category20();

  d3.layout.cloud().size([700, 700])
      .words(gword)
      .rotate(function() { return ~~(Math.random() * 2) * 90; })
      .font("Impact")
      .fontSize(function(d) { return d.size; })
      .on("end", draw)
      .start();

  function draw(words) {
    d3.select("body").append("svg")
        .attr("width", 700)
        .attr("height", 700)
      .append("g")
        .attr("transform", "translate(350,350)")
      .selectAll("text")
        .data(words)
      .enter().append("text")
        .style("font-size", function(d) { return d.size + "px"; })
        .style("font-family", "Impact")
        .style("fill", function(d, i) { return fill(i); })
        .attr("text-anchor", "middle")
        .attr("transform", function(d) {
          return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .text(function(d) { return d.text; });
  }
</script>
''')
    fhand2.write("\n];\n")
    fhand2.close()
    #pdfkit.from_url("http://google.com", r"C:\Users\Victor Deng\Desktop\Myreport\out.pdf", configuration=config)
    pdfkit.from_file(r"C:/Users/Victor Deng/Desktop/DataScience/Dreamdata --UCSC/"+ftitle+".htm", r"C:/Users/Victor Deng/Desktop/DataScience/Dreamdata --UCSC/output/"+ftitle+".pdf", configuration=config)
    print("Output written to gword.js")
    print("Open gword.htm in a browser to see the vizualization")

