import json
import sys

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    scoresNew = {}
    scoresCount = {}
    for line in sent_file:
      term, score = line.split("\t") # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score) # Convert the score to an integer.
    for line in tweet_file:
      converted = json.loads(line)
      tweet = converted.get('text',"").encode('UTF-8')
      s = 0
      for i in range(len(tweet.split())):
        word = tweet.split()[i]
# print word
        if word in scores:
          s = s + scores[word]
#      print s
      if s != 0:
        for i in range(len(tweet.split())):
          word = tweet.split()[i]
          if word not in scores:
            if word in scoresNew:
              scoresNew[word] = scoresNew[word] + s
              scoresCount[word] = scoresCount[word] + 1
            else:
              scoresNew[word] = s
              scoresCount[word] = 1
    for i in range(len(scoresNew)):
      print '{} {}'.format(scoresNew.keys()[i], scoresNew.values()[i])

if __name__ == '__main__':
    main()
