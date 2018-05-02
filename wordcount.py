import operator

class WordCount(object):

    def __init__(self, inputString):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        self.wordCount = self.h(inputString)

    def counter(self, l):
        result = {}
        for word in l:
            result.setdefault(word, 0)
            result[word] += 1

        return result

    def h(self, s):
        scores = self.counter(s.split())
        scores = sorted(scores.items(), key=operator.itemgetter(1))
        scores = reversed(scores)
        scores = list(x[0] for x in scores)
        return scores[0:10]