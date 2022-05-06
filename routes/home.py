from bottle import get, view, request, response, redirect
import data
import json
import jwt

##############  HOME  ################
@get('/<user_id>')
@view('home')
def _(user_id):

    try:
        # SESSSION
        user_session_jwt = request.get_cookie("jwt_user")
        if user_session_jwt not in data.SESSION:
            return redirect("/login") 
        
        for session in data.SESSION:
            if session == user_session_jwt:
                jwt_user = jwt.decode(session, data.JWT_USER_SECRET, algorithms=["HS256"])

        tweets=[]
        for key in reversed(list(data.TWEETS.keys())): 
            tweets.append(data.TWEETS[key])    
            tweet_id=data.TWEETS[key]
        # profile_picture_login

        # random users
        users = []
        for key in data.USERS:
            users_dict = data.USERS
            users.append(users_dict[key])
        
        is_fetch = True if request.headers.get('From-Fetch') else False
        return dict(
            title="Explore",
            is_fetch=is_fetch,
            tweet_id=tweet_id,

            tweets=tweets,

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


##############  TWEETS / GET  #################### 
@get('/tweets')
@view('home')
def _():
    try:
        # SESSSION
        user_session_jwt = request.get_cookie("jwt_user")
        if user_session_jwt not in data.SESSION:
            return redirect("/login") 

        tweets = []
        if data.TWEETS == {}:
            return {'info': 'No tweets found yet!'}
        
        # tweets
        for key in reversed(list(data.TWEETS.keys())):
            tweets.append(data.TWEETS[key])

        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(dict(tweets=tweets))
 
    except jwt.exceptions.InvalidTokenError as ex:
        print(ex)
        response.delete_cookie("jwt_user")
        return redirect("/login")