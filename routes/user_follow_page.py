from bottle import get, request, response, view, redirect
import data
import random
import jwt


###### Get following user tweets / GET #########
@get('/user-home-page/<user_id>')
@view('user-follow-page')
def _(user_id):
    try:

        user_session_jwt = request.get_cookie("jwt_user")
        if user_session_jwt not in data.SESSION:
            return redirect("/login") 
        
        for session in data.SESSION:
            if session == user_session_jwt:
                jwt_user = jwt.decode(session, data.JWT_USER_SECRET, algorithms=["HS256"])

        # local users
        local_users = []
        for key in data.USERS:
            users_dict = data.USERS
            local_users.append(users_dict[key])
            
        
        # user followers
        for key in data.USERS:
            if jwt_user['jwt_user_id'] in data.USERS[key]['user_id']:
                following_count = len(data.USERS[key]['user_following'])

        # user tweets
        user_tweets = []
        if user_id in data.USERS:
            followings = data.USERS[user_id]['user_following']

            for follow_id in followings:
                for key in data.TWEETS:
                    if follow_id == data.TWEETS[key]['user_id']:

                        user_tweets.append(data.TWEETS[key])

        is_fetch = True if request.headers.get('From-Fetch') else False               
        return dict(
                    is_fetch=is_fetch,
                    title="people-you-follow",

                    user_tweets=user_tweets,

                    tabs=data.tabs, 
                    trends=data.trends, 
                    items=data.items,
                    
                    following_count=following_count,
                    local_users=local_users,
                    jwt_user=jwt_user
                    )

    except jwt.exceptions.InvalidTokenError as ex:
        print(ex)
        response.delete_cookie("jwt_user")
        return redirect("/login")