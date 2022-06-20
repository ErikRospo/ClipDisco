import re

##song lyrics converter

markerRemover = re.compile(r'\[.*?\]')

lyricFile=open('rainog.txt','r')
outputfile=open('output.py','w')

lyrics=lyricFile.read()

cleanedLyrics=re.sub(markerRemover,'',lyrics)
lyricsList=cleanedLyrics.split("\n")
while "" in lyricsList:
    lyricsList.remove("")

out=""
out+="a={\n"
for n in range(1,len(lyricsList)+1):
    out+="\t"
    out+=str(n*100)
    out+=": [\""
    out+=lyricsList[n-1]
    out+="\"],\n"
out=out[0:-2]+"\n}"
outputfile.write(out)
lyricFile.close()
outputfile.close()