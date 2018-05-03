import operator

class WordCount(object):

    def __init__(self, inputString):
        self.wordCount = self.getFrequentWordsFrom(inputString)

    def getWordCounts(self, wordList):
        result = {}
        for word in wordList:
            result.setdefault(word, 0)
            result[word] += 1

        return result

    def getFrequentWordsFrom(self, s):
        wordNumberToReturn = 10 #the number of most common words that you'd like to return

        words = s.split()     #turn string into a list of words in the string
        words = [x.lower() for x in words] #turn all words in the list to lowercase, to easily take out words we don't want

        stopwords = ['the', 'i', 'from', 'a', 'me', 'thing', 'is', 'of', 'by', 'be', 'any', 'on', 'my', 'and', 'in', 'are', 'https:', '...', '-'] #words we don't want
        for word in list(words):
            if word in stopwords:
                words.remove(word) #remove the words we don't want

        scores = self.getWordCounts(words)   #magic that gets the most frequent words in the list
        scores = sorted(scores.items(), key=operator.itemgetter(1))
        scores = reversed(scores)
        scores = list(x[0] for x in scores)

        return scores[0:wordNumberToReturn]