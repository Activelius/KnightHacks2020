import base64
import tweepy
import random

CONSUMER_KEY       = "CvjTnK7N3MKwDtzKbXoSjObdM"
CONSUMER_SECRET    = "GoRXp7EThS29ovRlg8kQjOZ92Uza6UjDi85udHFcu5ZCvJ4G9R"
OAUTH_TOKEN        = "1315096010264281088-mLisyhdWFlRd022kPGJ3pB6z47T3mf"
OAUTH_TOKEN_SECRET = "SSJ42yrBpR1qLIv6DtR0ugopVDQLJzc3Co0kQoq9v5mK5"

def postimage(event, context):
     """Triggered from a message on a Cloud Pub/Sub topic.
          Args:
          event (dict): Event payload.
          context (google.cloud.functions.Context): Metadata for the event.
     """
     pubsub_message = base64.b64decode(event['data']).decode('utf-8')

     auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
     auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
     
     api = tweepy.API(auth)

     me = api.me()

     index = me.statuses_count % 100

     image_url = "https://github.com/Activelius/KnightHacks2020/tree/main/processed_images/%d.png" % 
index

     starters = ["Have.... another one ", "Here ya go ", "Still working hard ", "Doodling, doodling, 
doodling "]

     knighthacks_string = "#00%d %s @GithubEducation #MyOctocat @ knighthacks %s" % 
(me.statuses_count, starters[ random.randint(0,len(starters)-1) ], image_url)

     api.update_status(knighthacks_string)
     
     print(pubsub_message)

