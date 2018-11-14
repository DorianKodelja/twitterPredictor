from twitter_collect import twitter_connection_setup
from tweepy.streaming import StreamListener
import tweepy

def get_candidate_queries(num_candidate, file_path,file_type):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    queries=[]

    keywords_file_path="{}_{}_candidate_{}.txt".format(file_path,file_type,num_candidate)
    try:
        with open(keywords_file_path,'r') as keyword_file:
            keywords=keyword_file.read().split("\n")

        i=0
        for keyword1 in keywords:
            if file_type == "hashtag":
                queries.append("#{}".format(keyword1))
            else:
                queries.append("{}".format(keyword1))
            if i <len(keywords)-2:
                for keyword2 in keywords[i+1:]:
                    if file_type == "hashtag":
                        queries.append("#{} AND #{}".format(keyword2, keyword2))
                    else:
                        queries.append("{} AND {}".format(keyword2, keyword2))
            i = i + 1

        return queries

    except IOError:
        print("file {} is missing.".format(keywords_file_path))
        return []
        # TO COMPLETE


def get_tweets_from_candidates_search_queries(queries, twitter_api):


    all_tweets=[]
    try:
        for query in queries:
            tweets = twitter_api.search(query, lang="french", rpp="20")
            for tweet in tweets:
                all_tweets.append(tweet)

    except tweepy.TweepError as e:

        if e.response.text in ["429","420"]:
            print("we exceeded the twitter rate limit, returning now")
            return all_tweets
        elif e.response.text =="500":
            print("Twitter down, Twitter down!")
            return None
        elif  e.response.text =="401":
            print("wrong credentials!")
            return None
        elif  e.response.text =="404":
            print("The request <{}> is invalid".format(query))
            return None
        else:
            "twitter API responded with code {}, something is wrong ".format(e.response.text)
            return None

    return all_tweets


def get_replies_to_candidate(num_candidate,twitter_api):
    tweets_and_replies=[]
    statuses = twitter_api.user_timeline(id=num_candidate, count="20")
    for status in statuses:
        curr_tweet_replies=[]

        print(status.text)
    return statuses


