
from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too



# putting form together


@app.route("/", methods=['POST'])
def error():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify_password']
    email = request.form['email']
    if username == "" or (" " in username) or (username.count(" ") !=0):
        user_error = "Please enter a valid username"    
        return render_template("index.html", user_error=user_error)
    if len(username) < 3 or len(username) > 20:
        user_error = "Username must have between 3 and 20 characters"
        return render_template("index.html", user_error=user_error)  
    if password == "" or (" " in password) or (password.count(" ") !=0):
        pass_error = "Please enter a valid password"
        return render_template("index.html", pass_error=pass_error)
    if len(password) < 3 or len(password) > 20:
        pass_error = "Password must have between 3 and 20 characters"
        return render_template("index.html", pass_error=pass_error)  

    if verify != password:
        verify_error = "Passwords don't match"
        return render_template("index.html", verify_error=verify_error)
    
    if len(email) > 0 and ((email.count ("@") != 1) or (email.count(".") !=1) or (email.count (" ") !=0) or 
            (len(email) < 3) or (len(email) > 20)):
        email_error = "Please enter a valid email address" 
        return render_template("index.html", email_error=email_error)


    
    else:
        
        return render_template("welcome.html",username=username)

  

@app.route("/")
def index():
    username= request.args.get("username")
    return render_template('index.html', username=username) 

    # if we have an error, make a <p> to display it
   

    # combine all the pieces to build the content of our response
    


    


app.run()