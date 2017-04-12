#import regex
import re

#start process_tweet
def processTweet(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    return tweet
#end
#stopwordslist 
def getStopWordList(whatever) :
    
    stopwords = []
    fp = open(whatever, 'r')
    line = fp.readline()

    while line:
        line = line.strip('\n')
        stopwords.append(line)
        line = fp.readline()

    fp.close()
    return stopwords

def replaceTwoOrMore(i) :
    
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1" , i)

stopwords = getStopWordList('stopwordslist.txt')
#print(stopwords)
def getFeatureVector(tweet):
    
    featurevector = []
    words = tweet.split()
    for i in words:
        i = replaceTwoOrMore(i)
        i = i.strip('\'".?,!') #remove punctuation
        i = i.lower()
        if(i in stopwords):
            continue
        else:
            featurevector.append(i)
    
    return featurevector
    