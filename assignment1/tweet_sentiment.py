import sys
import json

def hw():
    print 'Hello, world!'

def lines1(fp):
    print str(len(fp.readlines()))

def parseSentiFile():
    afinnfile = open("./AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    print scores.items() # Print every (term, score) pair in the dictionary


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines1(sent_file)
    #lines1(tweet_file)

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    tweet_text = []
    tweet_score = 0
  
    lines = tweet_file.readlines()
    for keyt in lines:
        try:
            tweet = json.loads(keyt)
            if tweet.has_key('text'):
                txt = tweet['text']
                tweet_text.append(txt)
                #print tweet_text
        except ValueError:
            pass
    #print type(tweet_text) -->list
    #print len(tweet_text[:10])
    #print tweet_text[0]
    
    for item in tweet_text[25:39]:
        #print tweet_text[0]
        item = item.encode('utf-8')
        twords = str(item).split()
        print str(item)
         
        for words in twords:
            #unicode_words = words.encode('ascii', "ignore")
            #print unicode_words
            try:
                if scores.has_key(words):
                    tweet_score += scores[words]
                else:
                    pass
            except:
                pass
        if tweet_score != 0: 
            print float(tweet_score)

    #print float(tweet_score)
    sent_file.close()
    tweet_file.close()

            

if __name__ == '__main__':
    main()
    #map(maintest, range(10))
    #parseSentiFile()
