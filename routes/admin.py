from bottle import get, response, view, request, redirect
import data
import jwt

############## ADMIN PAGE / GET ##############
@get('/admin-page')
@view('admin')
def _():

    try:
        # SESSSION
        admin_session_jwt = request.get_cookie("jwt_admin")
        if admin_session_jwt not in data.SESSION:
            return redirect("/login") 

        
        if data.TWEETS == {}:
            return {'info': 'No tweets found yet!'}
        
        # tweets
        tweets = []
        for key in reversed(list(data.TWEETS.keys())):
            tweets.append(data.TWEETS[key])
        
        #response.content_type = 'application/json; charset=UTF-8'
        return dict(tweets=tweets)

    except jwt.exceptions.InvalidTokenError as ex:
        print(ex)
        response.delete_cookie("jwt_admin")
        return redirect("/login")