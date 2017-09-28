
from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too



# putting form together









@app.route("/", methods=['POST'])
def username_error():
    username = request.form['username']

    if username == "":
        error = "Please enter a valid username"    
        return redirect('/?error=' + error)
    
    

  
    
    

@app.route("/")
def index():
    render_template('submit.html', )

    # if we have an error, make a <p> to display it
   

    # combine all the pieces to build the content of our response
    


    


app.run()