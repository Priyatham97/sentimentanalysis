import training
import main
import nltk
# Test the classifier
testTweet = "i dont know its good"
processedTestTweet = main.processTweet(testTweet)
print (training.NBClassifier.classify(training.extract_features(main.getFeatureVector(processedTestTweet)))) 

