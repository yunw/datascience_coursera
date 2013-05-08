import oauth2 as oauth
import urllib2 as urllib
import json, sys

# See Assginment 6 instructions or README for how to get these credentials
access_token_key = "496890955-JLWjmXaXvCC2KiNh1kBqi8Xm0rbq3QHuMvxV9oq4"
access_token_secret = "QfgZnAJaxLtM8BxQHyAYgAupHPfRsP9nZTH3P8fskw"

consumer_key = "Xqf8uXqimyupDWp4sgdmTQ"
consumer_secret = "8c485JUCXGsVR9FXjppxZBBAFQdaoBPwMnFSUYj0Q"

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
  #print json.load(response).keys()
  tweet_text = []
  for line in response:
    try:
      tweet = json.loads(line)
      if tweet.has_key("text"):
        continue
      text = tweet["text"]
      tweet_text.append(text)
    except ValueError:
      pass
    
  print tweet_text
    
def afin2dic():
  afinnfile = open("AFINN-111.txt")
  scores = {} # initialize an empty dictionary
  for line in afinnfile:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.
  print scores.items() # Print every (term, score) pair in the dictionary

def lines(fp):
    print str(len(fp.readlines()))
 

def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])

  tweet_text = []
  
  for line in tweet_file:
    try:
      tweet = json.loads(line)
      if tweet.has_key("text"):
        continue
      text = tweet["text"]
      tweet_text.append(text)
      
    except ValueError:
      pass
    
  print 
  
if __name__ == '__main__':
  fetchsamples()
  #afin2dic()
  #main()
