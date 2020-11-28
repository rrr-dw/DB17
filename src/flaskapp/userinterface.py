from flask import (render_template,
                    request,
                    redirect,
                    url_for,
                    session)
from flaskapp import app,account


def render_template_UI(*argv, **kargv):
    return render_template(*argv,**kargv, user=account.get_session(),ni=get_navitems())

def render_template_error_UI(status_code):
    return render_template("error.html",status_code= status_code)

_navitems={
    "guest":[("Sign Up","signup"),("Sign In","signin")],
    "member":[("Sign Out","signout"),("My Account","myaccount")],

    "admin":[("Overview","tskstat"),
            ("Create Task","tskcreate"),
            ("Manage Task","tskmgmt"),
            ("Manage Users","usrmgmt")],
    "evaluator":[],
    "submitter":[],
}
def get_navitems():
    if not account.is_loggedin():
        return _navitems["guest"]
    else:
        return _navitems[account.get_role()]+_navitems["member"]