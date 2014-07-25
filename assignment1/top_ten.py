import json
import sys
import operator

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hashtags = {} # initialize an empty dictionary
    for line in tweet_file:
      converted = json.loads(line)
      hashtag = ""
      if 'entities' in converted:
        if len(converted['entities']['hashtags']) > 0:
          for i in range(len(converted['entities']['hashtags'])):
            hashtag = converted['entities']['hashtags'][i-1]['text'].encode('UTF-8')
        if hashtag != "":
          if hashtag in hashtags:
            hashtags[hashtag] = hashtags[hashtag] + 1
          else:
            hashtags[hashtag] = 1
    sortedHashtags = sorted(hashtags.iteritems(), key=operator.itemgetter(1), reverse=True)
    for i in range(10):
      print '{} {}'.format(sortedHashtags[i][0], sortedHashtags[i][1])

if __name__ == '__main__':
    main()
