from bottle import get, response, view, request, redirect
import data
import random
import jwt
import json

############## USER TWEETS / GET ##############
@get('/user-profile/<user_id>')
@view('user-profile')
def _(user_id):

    try:
        user_session_jwt = request.get_cookie("jwt_user")
        if user_session_jwt not in data.SESSION:
            return redirect("/login") 
        
        for session in data.SESSION:
            if session == user_session_jwt:
                jwt_user = jwt.decode(session, data.JWT_USER_SECRET, algorithms=["HS256"])

        if user_id in data.USERS:
            user_profile = data.USERS[user_id]
       
        if data.TWEETS == {}:
            return {'info': 'No tweets found yet!'}

        # local users
        users = []
        for key in data.USERS:
            users_dict = data.USERS
            users.append(users_dict[key])
            
        # get user_tweet by ID  
        user_tweets = []         
        for key in reversed(list(data.TWEETS.keys())): 
            if user_id in data.TWEETS[key]['user_id']:
                user_tweets.append(data.TWEETS[key])
        
        # user tweet - count
        tweet_count = 0
        for key in data.TWEETS:
            if user_id in data.TWEETS[key]['user_id']:
                tweet_count += 1

        # user follower - count
        for key in data.USERS:
            if user_id in data.USERS[key]['user_id']:
                follower_count = len(data.USERS[key]['user_followers'])
                following_count = len(data.USERS[key]['user_following'])

        #response.content_type = 'application/json; charset=UTF-8'
        is_fetch = True if request.headers.get('From-Fetch') else False
        return dict(
                    is_fetch=is_fetch,
                    title="Profile",

                    user_id=user_id,

                    user_tweets=user_tweets,

                    tweet_count=tweet_count,
                    follower_count=follower_count,
                    following_count=following_count,

                    user_profile=user_profile,

                    tabs=data.tabs, 
                    trends=data.trends, 
                    items=data.items,

                    local_users=users,
                    jwt_user=jwt_user,

                    )
                
    except jwt.exceptions.InvalidTokenError as ex:
        print(ex)
        response.delete_cookie("jwt_user")
        return redirect("/login")

    

############## USER COVER IMAGE / GET - ID ##############
@get('/user_cover_image_upload')
@view('user-cover-image')
def _():

    try:
        user_session_jwt = request.get_cookie("jwt_user")
        if user_session_jwt not in data.SESSION:
            return redirect("/login") 
        
        for session in data.SESSION:
            if session == user_session_jwt:
                jwt_user = jwt.decode(session, data.JWT_USER_SECRET, algorithms=["HS256"])
        
        user_id = jwt_user['jwt_user_id']

        is_fetch = True if request.headers.get('From-Fetch') else False
        page_title = "upload-cover"
        return dict(
            title=page_title,
            is_fetch=is_fetch,

            jwt_user=jwt_user,
            user_id=user_id
        )
    except jwt.exceptions.InvalidTokenError as ex:
        print(ex)
        response.delete_cookie("jwt_user")
        return redirect("/login")