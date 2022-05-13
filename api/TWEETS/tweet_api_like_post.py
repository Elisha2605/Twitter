from bottle import post, response, request, redirect
import json
import data
import jwt


@post('/tweet-api-like/<tweet_id>')
def _(tweet_id):

    try:
        user_session_jwt = request.get_cookie("jwt_user")
        if user_session_jwt not in data.SESSION:
            return redirect("/login") 
        
        for session in data.SESSION:
            if session == user_session_jwt:
                jwt_user = jwt.decode(session, data.JWT_USER_SECRET, algorithms=["HS256"])

        if jwt_user['jwt_user_id'] in data.TWEETS[tweet_id]['tweet_likes']:
            data.TWEETS[tweet_id]['tweet_likes'].remove(jwt_user['jwt_user_id'])
            message = "dislike"
        else :
            data.TWEETS[tweet_id]['tweet_likes'].append(jwt_user['jwt_user_id'])
            message = "Like"

        likes_count = len(data.TWEETS[tweet_id]['tweet_likes'])
        
        # response.content_type = 'application/json; charset=UTF-8'
        return dict(tweet_liked=data.TWEETS[tweet_id], likes_count=likes_count)
        # return dict(message=message, likes_count=likes_count)

    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}