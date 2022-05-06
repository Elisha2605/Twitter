from bottle import post, response, request, redirect, get, view
import data
import jwt
import json


################  USER FOLLOW  ######################
@post('/api-user-follow/<user_id>')
def _(user_id):

    try:

        user_session_jwt = request.get_cookie("jwt_user")
        if user_session_jwt not in data.SESSION:
            return redirect("/login") 
        
        for session in data.SESSION:
            if session == user_session_jwt:
                jwt_user = jwt.decode(session, data.JWT_USER_SECRET, algorithms=["HS256"])     
            
        # don't follow yourself
        if user_id == jwt_user['jwt_user_id']:
            print('#'*100)
            print("You cant't follow yourself")
            return "You cant't follow yourself"

        # Unfollow
        if user_id in data.USERS[jwt_user['jwt_user_id']]['user_following']:
            data.USERS[jwt_user['jwt_user_id']]['user_following'].remove(user_id)
            data.USERS[user_id]['user_followers'].remove(jwt_user['jwt_user_id'])
            print('#'*100)
            message = f"unfollowing user: , {user_id} - {data.USERS[user_id]['user_first_name']}"
            print(message)
            isfollow = "Follow"
            response.content_type = 'application/json; charset=UTF-8'
            return json.dumps(dict(server_message=isfollow, jwt_user=jwt_user))

        # Follow 
        if user_id in data.USERS:
            #from
            data.USERS[user_id]['user_followers'].append(jwt_user['jwt_user_id'])
            #to
            data.USERS[jwt_user['jwt_user_id']]['user_following'].append(user_id)
            jwt_user['jwt_user_following'].append(user_id)

            print('#'*100)
            message = f"following user: , {user_id} - {data.USERS[user_id]['user_first_name']}"
            print(message)
            isfollow = "Unfollow"
            response.content_type = 'application/json; charset=UTF-8'
            return json.dumps(dict(server_message=isfollow, jwt_user=jwt_user))
               

    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}