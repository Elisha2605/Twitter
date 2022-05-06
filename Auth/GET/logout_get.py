from bottle import get, request, response, redirect
import data
import jwt


####################  Logout User / GET  ######################
@get('/logout')
def _():
    try: 
        if not request.get_cookie("jwt_user"):
            return redirect("/login")
        
        user_session_jwt = request.get_cookie("jwt_user")
        data.SESSION.remove(user_session_jwt)

        response.delete_cookie('jwt_user')
        return redirect('/login')
    except jwt.exceptions.InvalidTokenError as ex:
        print(ex)
        response.delete_cookie("jwt_user")
        return redirect("/login")
        
####################  Logout Admin / GET  ######################
@get('/logout-admin')
def _():

    try: 
        if not request.get_cookie("jwt_admin"):
                return redirect("/login")
        
        admin_session_jwt = request.get_cookie("jwt_admin")
        data.SESSION.remove(admin_session_jwt)

        response.delete_cookie('jwt_admin')
        return redirect('/login')
    
    except jwt.exceptions.InvalidTokenError as ex:
        print(ex)
        response.delete_cookie("jwt_admin")
        return redirect("/login")