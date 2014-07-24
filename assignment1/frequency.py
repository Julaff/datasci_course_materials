import json
import sys

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    freq = {} # initialize an empty dictionary
    numWords = 0
    for line in tweet_file:
      converted = json.loads(line)
      tweet = converted.get('text',"").encode('UTF-8')
      for i in range(len(tweet.split())):
        word = tweet.split()[i]
        numWords = numWords + 1
# print word
        if word in freq:
          freq[word] = freq[word] + 1
        else:
          freq[word] = 1
#    print freq.items()
    for i in range(len(freq)):
      freqValue = float(freq.values()[i]) / numWords
      print '{} {}'.format(freq.keys()[i], freqValue)


if __name__ == '__main__':
    main()
