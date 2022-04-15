#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import make_response
from flask import render_template
from flask import redirect
from flask import url_for

app= Flask(__name__)

# Got this data object from the Balldontlie API
hooper = {
  "id":237,
  "first_name":"LeBron",
  "last_name":"James",
  "position":"F",
  "height_feet": 6,
  "height_inches": 8,
  "weight_pounds": 250,
  "team":{
    "id":14,
    "abbreviation":"LAL",
    "city":"Los Angeles",
    "conference":"West",
    "division":"Pacific",
    "full_name":"Los Angeles Lakers",
    "name":"Lakers"
  }
}


@app.route("/login")
@app.route("/")
def index():
    return render_template("hooperinfo.html")
# set the cookie and send it back to the user
@app.route("/setcookie", methods = ["POST", "GET"])
def setcookie():
    # if user generates a POST to our API
    if request.method == "POST":
        if request.form.get("nm"): # if nm was assigned via the POST
            user = request.form.get("nm") # grab the value of nm from the POST
        else: # if a user sent a post without nm then assign value defaultuser
            user = "defaultuser"

        resp = make_response(render_template("readcookie.html"))
        resp.set_cookie("userID", user)

        # return our response object includes our cookie
        return resp
        
    if request.method == "GET": # if the user sends a GET
        return redirect(url_for("index")) # redirect to index

# check users cookie for their name
@app.route("/getcookie")
def getcookie():
    # attempt to read the value of userID from user cookie
    name = request.cookies.get("userID") # preferred method
    
    # name = request.cookies["userID"] # <-- this works but returns error
    # if value userID is not in cookie
    
    # return HTML embedded with name (value of userID read from cookie) 
    return f'<h1>Heard you love hoops, {name}. </h1>'

@app.route("/info")
def info():
    return jsonify(hooper)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)