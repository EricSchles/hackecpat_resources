from flask import Flask, render_template, jsonify, redirect, url_for, request
import json
import sys
app = Flask(__name__)

@app.route("/get_data",methods=["GET","POST"])
def get_data():
    if request.method=="GET":
        print "You sent a get request to the server"
        print "Getting you some json :)"
        get_req = json.load(open("get_req.json","r"))
        print json.dumps(get_req)
        return json.dumps(get_req)
    if request.method=="POST":
        print "You sent a post request to the server"
        print "Getting you some json :-)"
        post_req = json.load(open("post_req.json","r"))
        return json.dumps(post_req)
    else:
        return "I didn't understand your request"

#@app.route("/send_data",methods=["GET","POST"])
@app.route("/send_data/<data>",methods=["GET","POST"])
def send_data(data):
    if request.method=="POST":
        data = json.loads(data)
        data_store = json.load(open("saved_data.json","r"))
        data_store.update(data)
        json.dump(data_store,open("saved_data.json","w"))
        return "worked"
    else:
        print "only post request will work"

@app.route("/view_data",methods=["GET","POST"])
def view_data():
    if request.method=="GET":
        return json.load(open("saved_data.json","r"))
    return "please use a get request to access this data"
app.run(debug=True)
