import json
from pprint import pprint
import urllib2
import sys

if len(sys.argv) != 3:
        print "================== ERROR =================="
        print "\nDebes indicar como primer argumento el nombre del twittero sin '@' y como segundo argumento el numero de tweets a guardar";
	print "\nEjemplo: python save_tweets.py nombreusuario 40"
	print "\nEl ejemplo anterior guardara los ultimos 40 tweets del usuario 'nombreusuario'"
	print "================== ERROR =================="

else:
	f = open ("tweets.xls", "w") # w = sobreescribir todo.

	print "\nObteniendo tweets de ", sys.argv[1], ", espera por favor..."

	url = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=" + sys.argv[1] + "&count=" + sys.argv[2] + "&include_rts=true"

	#Hacemos la peticion
	tweets = urllib2.urlopen(url)
	data = json.load(tweets)
	#Recorremos los tweets y los escribimos en el fichero
	for tweet in data:
		f.write("\n")
		f.write(unicode(tweet["text"]).encode("utf-8"))

	print "\nLos tweets fueron guardados en el archivo tweets.xls"
	tweets.close()
	f.close()
