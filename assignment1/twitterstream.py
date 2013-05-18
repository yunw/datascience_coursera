import oauth2 as oauth
import urllib2 as urllib
import json, sys

# See Assginment 6 instructions or README for how to get these credentials
access_token_key =  
access_token_secret =  

consumer_key =  
consumer_secret =  

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://stream.twitter.com/1/statuses/sample.json"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    unicode_string = line.encode('utf-8')
    print unicode_string.strip()
 # print tweet_text
    
def afin2dic():
  afinnfile = open("AFINN-111.txt")
  scores = {} # initialize an empty dictionary
  for line in afinnfile:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.
  print scores.items() # Print every (term, score) pair in the dictionary

def lines(fp):
    print str(len(fp.readlines()))

# http://pastebin.com/bqj3bZhG

def fetchtweets():
  sent_file = open(sys.argv[1])
  filename = sys.argv[2]
  tweets_text = []
  
  f = file(filename, "r")
  
  lines = f.readlines().split()
  for item in lines:
    try:
      tweet = json.loads(item)
      text = tweet["text"]
      if text.find("rt ") > -1:
        continue
      if sent_file.key() in text:
        tweets_text.append( text )
      else:
        print
    except ValueError:
      pass

def affin():
  afinnfile = open("./AFINN-111.txt")
  scores = {} # initialize an empty dictionary
  for line in afinnfile:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.
  return scores

def main():
  #sent_file = open(sys.argv[1])
  #tweet_file = open(sys.argv[2])
  f = open(sys.argv[1])
  # type(f.readlines()) is a list, len(f.readlines())=1!!
  #print json.load(f)
  # type(f.readlines()[0]) is a str
  # type(json.loads(f.readlines()[0])) gets dict
  #Expecting property name: line 1 column 1 (char 1)--fixed by change
  # file to output-probl.log
  # json.loads(f.readlines()[0]).keys() get all fields
  #print json.loads(f.readlines()[0])['text']
 # for line in f:
    #print line

  afinnfile = open("./AFINN-111.txt")
  scores = {} # initialize an empty dictionary
  for line in afinnfile:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.


  tweet_text = []
  tweet_score = 0
  
  lines = f.readlines()
  #print type(json.loads(lines[0]))
  for item in lines:
    try:
      #print type(json.loads(item))-->dict
      #unicode_string = item.encode('utf-8')
      tweet = json.loads(item)
      '''
      print tweet['text']
      #.encode('utf-8')
      text = tweet['text']
      tweet_text.append(text)
      '''
      if tweet.has_key('text'):
       # continue
        #print tweet['text']
        txt = tweet['text']
        tweet_text.append(txt)
      else:
        print

    except ValueError:
      pass
    
  #print tweet_text
  for item in tweet_text:
        if item in scores:
            tweet_score += scores[item]
  print float(score)
    

  f.close()
    

  
  
  
if __name__ == '__main__':
  fetchsamples()
  #fetchtweets
  #afin2dic()
  #main()
