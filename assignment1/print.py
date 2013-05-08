import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
#print type(json.load(response))
#pyresp = json.load(response)
#print pyresp.keys()
#print json.load(response).keys()
#only can return for first time call because it's an object instance
#print dict value when key is 'results'
#print type(json.load(response)['results'])
#list
print json.load(response)['results']('text')
