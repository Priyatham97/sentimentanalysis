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

#Read the tweets one by one and process it
fp = open('sampleTweets.txt', 'r')
line = fp.readline()

while line:
    processedTweet = processTweet(line)
   # print (processedTweet)
    line = fp.readline()
#end loop
fp.close()

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

def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in featureList:
        features['contains(%s)' % word] = (word in tweet_words)
    return features

import csv
import nltk
#Read the tweets one by one and process it
inpTweets = csv.reader(open('something.csv', 'rt' , encoding="utf8"), delimiter=',', quotechar='"')
stopWords = getStopWordList('stopwordslist.txt')
featureList = []

# Get tweet words
tweets = []
for r in inpTweets:
    sentiment = r[0]
    tweet = r[1]
    processedTweet = processTweet(tweet)
    featureVector = getFeatureVector(processedTweet)
    featureList.extend(featureVector)
    tweets.append((featureVector, sentiment));
#end loop
# Remove featureList duplicates


# Extract feature vector for all tweets in one shote
training_set = nltk.classify.util.apply_features(extract_features, tweets)
# Train the classifier
NBClassifier = nltk.NaiveBayesClassifier.train(training_set)

# Test the classifier
testTweet = 'Congrats @ravikiranj, i heard you wrote a new tech post on sentiment analysis'
processedTestTweet = processTweet(testTweet)
print (NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet)))) 
