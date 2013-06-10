import bottle
import pymongo
import cgi
import re
import datetime
#import random
#import hmac
import user
import sys
from _dummy_thread import error

connection_string = "mongodb://localhost"


@bottle.route('/')
def recap_index():
    connection = pymongo.Connection(connection_string, safe=True)
    db = connection.recap
    accounts = db.accounts

    username = login_check()

    cursor = accounts.find().sort('date', -1).limit(10)

    print ('check', cursor)
    return bottle.template('recap_template',
             dict(myaccounts=cursor, username=username))


# gets called both for regular requests and json requests
@bottle.get("/account/<permalink>")
def show_account(permalink="notfound"):
    connection = pymongo.Connection(connection_string, safe=True)
    db = connection.recap
    accounts = db.accounts

    username = login_check()  # see if user is logged in
    permalink = cgi.escape(permalink)

    # determine if its a json request
    path_re = re.compile(r"^([^\.]+).json$")
    
    print ("about to query on permalink = ", permalink)
    
    
    account = accounts.find_one({'permalink':permalink})
    print('@this is account ',account)
    # end student work
    if account == None:
        bottle.redirect("/account_not_found")
    
    print ("date of entry is ", account['date'])

    # fix up date
    account['date'] = account['date'].strftime("%A, %B %d %Y at %I:%M%p")

   

    return bottle.template("entry_template", dict(account=account, username=username, errors=""))


# inserts the account entry and returns a permalink for the entry
def insert_entry(title, account, representative):
    print ("inserting new account", title, account)

    connection = pymongo.Connection(connection_string, safe=True)

    db = connection.recap
    accounts = db.accounts

    exp = re.compile('\W') # match anything not alphanumeric
    whitespace = re.compile('\s')
    temp_title = whitespace.sub("_",title)
    permalink = exp.sub('', temp_title)

    account = {"title": title, 
            "representative": representative,
            "account": account, 
            "permalink":permalink,         
            "date": datetime.datetime.utcnow()}
    
    print ('insert acc ',account)

    try:
      
        accounts.insert(account)
        print ("Inserting the account", account)


    except:
        print ("Error inserting account")
        print ("Unexpected error:", sys.exc_info()[0])

    return permalink

@bottle.get("/account_not_found")
def account_not_found():
    return ("Sorry, account not found")

@bottle.get('/newaccount')
def get_newaccount():

    username = login_check()  # see if user is logged in
    if (username == None):
        bottle.redirect("/login")        

    return bottle.template("newaccount", dict(title="", account="",errors="", username=username))

# put handler for setting up a new account
@bottle.post('/newaccount')
def account_newaccount():
    print ('hello')
    title = bottle.request.forms.get("title")
    print('title')
    account = bottle.request.forms.get("account")
    
    #title ='test2'
    #account ='jtestinformation2'
    
    print(title,' ', account)
    

    username = login_check()  # see if user is logged in
    if (username is None):
        
        bottle.redirect("/login")        
    
    if (title == "" or account == ""):
        errors="account must contain a title and account entry"
        return bottle.template("newaccount", dict(subject=cgi.escape(title, quote=True), username=username,
                                                 body=cgi.escape(account, quote=True),  errors=errors))

   
    
    # looks like a good entry, insert it escaped
    escaped_account = cgi.escape(account, quote=True) 
    print('esc',escaped_account)

    # substitute some <p> for the paragraph breaks
    newline = re.compile('\r?\n')
    formatted_account = newline.sub("<p>",escaped_account)
    
    permalink=insert_entry(title, formatted_account, username)
    print('perma',permalink)

    # now bottle.redirect to the account permalink
    bottle.redirect("/account/" + permalink)
    


# displays the initial account sign up form
@bottle.get('/signup')
def present_signup():
    return bottle.template("signup", 
                           dict(username="", password="", 
                                password_error="", 
                                email="", username_error="", email_error="",
                                verify_error =""))

# displays the initial account login form
@bottle.get('/login')
def present_login():
    return bottle.template("login", 
                           dict(username="", password="", 
                                login_error=""))

# handles a login request
@bottle.post('/login')
def process_login():

    connection = pymongo.Connection(connection_string, safe=True)

    username = bottle.request.forms.get("username")
    password = bottle.request.forms.get("password")

    print ("user submitted ", username, "pass ", password)

    userRecord = {}
    if (user.validate_login(connection, username, password, userRecord)):
        session_id = user.start_session(connection, username)
        if (session_id == -1):
            bottle.redirect("/internal_error")

        cookie = user.make_secure_val(session_id)

        
        bottle.response.set_cookie("session", cookie)
        
        bottle.redirect("/welcome")

    else:
        return bottle.template("login", 
                           dict(username=cgi.escape(username), password="", 
                                login_error="Invalid Login"))
        
        
@bottle.get('/internal_error')
@bottle.view('error_template')
def present_internal_error():
    return ({error:"System has encountered a DB error"})


@bottle.get('/logout')
def process_logout():

    connection = pymongo.Connection(connection_string, safe=True)

    cookie = bottle.request.get_cookie("session")

    if (cookie == None):
        print ("no cookie...")
        bottle.redirect("/signup")

    else:
        session_id = user.check_secure_val(cookie)

        if (session_id == None):
            print ("no secure session_id")
            bottle.redirect("/signup")
            
        else:
            # remove the session

            user.end_session(connection, session_id)

            print ("clearing the cookie")

            bottle.response.set_cookie("session","")


            bottle.redirect("/signup")


@bottle.post('/signup')
def process_signup():

    connection = pymongo.Connection(connection_string, safe=True)

    email = bottle.request.forms.get("email")
    username = bottle.request.forms.get("username")
    password = bottle.request.forms.get("password")
    verify = bottle.request.forms.get("verify")

    # set these up in case we have an error case
    errors = {'username':cgi.escape(username), 'email':cgi.escape(email)}
    if (user.validate_signup(username, password, verify, email, errors)):
        if (not user.newuser(connection, username, password, email)):
            # this was a duplicate
            errors['username_error'] = "Username already in use. Please choose another"
            return bottle.template("signup", errors)
            
        session_id = user.start_session(connection, username)
        print (session_id)
        cookie= user.make_secure_val(session_id)
        bottle.response.set_cookie("session",cookie)
        bottle.redirect("/welcome")
    else:
        print ("user did not validate")
        return bottle.template("signup", errors)


# will check if the user is logged in and if so, return the username. otherwise, it returns None
def login_check():
    connection = pymongo.Connection(connection_string, safe=True)
    cookie = bottle.request.get_cookie("session")

    if (cookie == None):
        print ("no cookie...")
        return None

    else:
        session_id = user.check_secure_val(cookie)

        if (session_id == None):
            print ("no secure session_id")
            return None
            
        else:
            # look up username record
            session = user.get_session(connection, session_id)
            if (session == None):
                return None

    return session['username']
    
@bottle.get("/welcome")
def present_welcome():
    # check for a cookie, if present, then extract value

    username = login_check()
    if (username == None):
        print ("welcome: can't identify user...redirecting to signup")
        bottle.redirect("/signup")

    return bottle.template("welcome", {'username':username})        



bottle.debug(True)
bottle.run(host='localhost', port=8082)
    
    
    
    
    
    
    