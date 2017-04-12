import classify
import nltk
from classify import *
  
inpfile = open("something.txt", "rt", encoding="utf8")
line = inpfile.readline()
count = 1
tweetItems = []
opinions = []
while line:    
    count += 1
    splitArr = line.split('|')
    processed_tweet = splitArr[1].strip()
    opinion = splitArr[0].strip()
    tweet_item = processed_tweet, opinion
    if(opinion != 'neutral' and opinion != 'negative' and opinion != 'positive'):
        print('Error with tweet = %s, Line = %s')
    tweetItems.append(tweet_item)    
    line = inpfile.readline()
#end while loop

tweets = []    
for (words, sentiment) in tweetItems:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, sentiment))

word_features = getSVMFeatureVector(tweets)
set_word_features(word_features)
training_set = nltk.classify.apply_features(extract_features, tweets)
    
classifier = nltk.NaiveBayesClassifier.train(training_set)
tweet = 'im so sad'
print (classifier.classify(extract_features(tweet.split())))
print (nltk.classify.accuracy(classifier, training_set))
classifier.show_most_informative_features(20)