from bottle import get, request, response, view,post
import data
import random


##############  USERS / GET  #################### 
@get('/api-users-tweets/<tweet_id>')
def _(tweet_id):
    try:

        return dict(tweets=data.TWEETS[tweet_id])
    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}

###### People you follow's tweets #########
@get('/api-user-follow-tweets/<user_id>')
def _(user_id):
    try:
        user_tweets = []
        if user_id in data.USERS:
            followings = data.USERS[user_id]['user_following']

            for follow_id in followings:
                for key in data.TWEETS:
                    if follow_id == data.TWEETS[key]['user_id']:

                        user_tweets.append(data.TWEETS[key])
                    
        return dict(tweets=user_tweets)

    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}

