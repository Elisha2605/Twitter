from bottle import get, response, view, request, redirect
import data
import jwt


############## USER TWEETS / GET - ID ##############
@get('/user-account/<user_id>')
@view('user-account')
def _(user_id):

    try:
         # SESSSION
        user_session_jwt = request.get_cookie("jwt_user")
        if user_session_jwt not in data.SESSION:
            return redirect("/login") 
        
        for session in data.SESSION:
            if session == user_session_jwt:
                jwt_user = jwt.decode(session, data.JWT_USER_SECRET, algorithms=["HS256"])
        
        
        if data.TWEETS == {}:
            return {'info': 'No tweets found yet!'}

        # get user_tweet by ID 
        user_tweets = []          
        for key in reversed(list(data.TWEETS.keys())): 
            if user_id in data.TWEETS[key]['user_id']:
                user_tweets.append(data.TWEETS[key])
        
        # local users
        users = []
        for key in data.USERS:
            users_dict = data.USERS
            users.append(users_dict[key])
       
        #response.content_type = 'application/json; charset=UTF-8'
        is_fetch = True if request.headers.get('From-Fetch') else False
        return dict(
                    is_fetch=is_fetch,
                    title="Home / My Account",

                    user_id=user_id,

                    user_tweets=user_tweets,

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