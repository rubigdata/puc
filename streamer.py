import settings
import tweepy
from textblob import TextBlob
from sqlalchemy.exc import ProgrammingError
import json
import sys

mentions = 0
majority = ""

def MJRTY(politician):
    global mentions
    global majority

    if mentions == 0:
	majority = politician
	mentions = 1
    elif politician == majority:
	mentions += 1
    else:
	mentions -= 1

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):

        description = status.user.description
        loc = status.user.location
        text = status.text
        coords = status.coordinates
        geo = status.geo
        name = status.user.screen_name
        user_created = status.user.created_at
        followers = status.user.followers_count
        id_str = status.id_str
        created = status.created_at
        retweets = status.retweet_count
        bg_color = status.user.profile_background_color
        blob = TextBlob(text)
        sent = blob.sentiment

        if geo is not None:
            geo = json.dumps(geo)

        if coords is not None:
            coords = json.dumps(coords)

        print text
	tokens = map (unicode.lower, text.split())
	for p in settings.TRACK_TERMS:
            if p in tokens:
                MJRTY(p)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

auth = tweepy.OAuthHandler(settings.TWITTER_APP_KEY, settings.TWITTER_APP_SECRET)
auth.set_access_token(settings.TWITTER_KEY, settings.TWITTER_SECRET)
api = tweepy.API(auth)

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)

try:
    stream.filter(track=settings.TRACK_TERMS)
except KeyboardInterrupt:
    print "Meerderheid mentions: " + majority if mentions > 0 else "No majority"
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

