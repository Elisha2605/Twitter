from bottle import get, view, request, response


##############  Index  ################
@get('/')
@view('index')
def _():

    try:
        is_fetch = True if request.headers.get('From-Fetch') else False
        return dict(
            title="Twitter",
            is_fetch=is_fetch,
        )
    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}