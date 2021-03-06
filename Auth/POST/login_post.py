from bottle import post, request, redirect, response
import data
import uuid
import re
import jwt


####################  Login / POST  ######################
@post('/login')
def _():
    
    # VALIDATION
    if not request.forms.get("user_email"):
        response.status = 400
        return redirect("/login?error=user_email")
        
        
    if not re.match(data.REGEX_EMAIL, request.forms.get("user_email")):
        response.status = 400
        return redirect("/login?error=user_email")  
    
        
    user_email = request.forms.get("user_email")
    user_password = request.forms.get("user_password")
      
    if not request.forms.get("user_password"):
        response.status = 400
        return redirect(f"/login?error=user_passowrd&user_email={user_email}")
    if not 2 <= len(user_password) <= 30:
        response.status = 400
        return redirect(f"/login?error=user_password&user_email={user_email}")  

    # Login User
    for key in data.USERS:
        user_id = key
        if request.forms.get("user_email") == data.USERS[key]['user_email']:
            if request.forms.get("user_password") == data.USERS[key]['user_password']:
                
                # COOKIES 
                encode_user_jwt = jwt.encode({
                    'jwt_user_id': data.USERS[key]['user_id'],
                    'jwt_user_first_name': data.USERS[key]['user_first_name'], 
                    'jwt_user_last_name': data.USERS[key]['user_last_name'], 
                    'jwt_user_name': data.USERS[key]['user_name'], 
                    'jwt_user_profile_picture': data.USERS[key]['user_profile_picture'],
                    'jwt_user_cover_image': data.USERS[key]['user_cover_image'],
                    'jwt_user_signup_date': data.USERS[key]['user_signup_date'],
                    'jwt_user_following': data.USERS[key]['user_following'],
                    'session_id': str(uuid.uuid4())
                },
                    data.JWT_USER_SECRET, algorithm="HS256"
                )

                data.SESSION.append(encode_user_jwt)

                # SET COOKIE
                response.set_cookie('jwt_user', encode_user_jwt)

                response.status = 200
                return redirect(f'/{user_id}')
            else: 
                response.status = 400
                return redirect(f"/login?error=user_password&user_email={user_email}")  
    # Login Admin
    if request.forms.get("user_email") == data.ADMIN['admin_email']:
        if request.forms.get('user_password') == data.ADMIN['admin_password']:

            encode_admin_jwt = jwt.encode({
                'admin_id': data.ADMIN['admin_id'],
                'admin_name': data.ADMIN['admin_id'],
                'session_id': str(uuid.uuid4())
            },
                data.JWT_ADMIN_SECRET, algorithm="HS256"
            )
            data.SESSION.append(encode_admin_jwt)

            # SET COOKIE
            response.set_cookie('jwt_admin', encode_admin_jwt)

            ######### test
            print('#'*100)
            print("From /login")
            print(data.SESSION)

            response.status = 200
            return redirect('/admin-page')
        else:
            response.status = 400
            return redirect(f"/login?error=user_password&user_email={user_email}")  
    

    return redirect("/login?error=user_email")  