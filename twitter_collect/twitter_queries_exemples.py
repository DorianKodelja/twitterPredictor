import twitter_connection_setup
from tweepy.streaming import StreamListener
import tweepy
#collecte "nb_tweets" tweets en langue "lang" correspondant à la query "query"
def collect_and_print(query,lang="french",nb_tweets=100,verbose=False):
    connexion = twitter_connection_setup.twitter_setup()

    #cherche des tweets contenant "emmanuel macron"
    # query="emmanuel Macron"


    #cherche des tweets contenant "emmanuel and macron"
    #query="Emmanuel and Macron"

    #cherche des tweets contenant "emmanuel" ET "macron"
    #query="Emmanuel AND Macron"

    #cherche des tweets contenant "emmanuel" ou "macron" (ou les deux)
    #query="Emmanuel OR Macron"


    #cherche des tweets contenant "emmanuel" mais pas "macron"
    #query="Emmanuel -Macron"


    #cherche des tweets contenant le hashtag "#EmmanuelMacron"
    #query="#EmmanuelMacron"

    #cherche des tweets mentionnant l'utilisateur @EmmanuelMacron
    # query="@EmmanuelMacron"

    tweets = connexion.search(query,lang=lang,rpp=nb_tweets)
    if verbose:
        for tweet in tweets:
            print(tweet.text)
    return tweets


#collecte les tweets de l'utilisateur 374392774
def collect_by_user(user_id="374392774",count=200,verbose=False):
    connexion = twitter_connection_setup.twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = count)
    if verbose:
        for status in statuses:
            print(status.text)
            from IPython import embed;import inspect;embed(header="{}".format(inspect.getframeinfo(inspect.currentframe())[:3]))
    return statuses

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True


#affiche en temps reel les nouveaux tweets contenant la chaine quer
#voir http://docs.tweepy.org/en/v3.6.0/streaming_how_to.html?highlight=streaming
def collect_by_streaming(query="Emmanuel Macron"):
    connexion = twitter_connection_setup.twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(track=[query])

def collect_user_by_streaming(user_id="374392774"):
    connexion = twitter_connection_setup.twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(follow=[user_id])


collect_by_user(verbose=True)
print("ok")