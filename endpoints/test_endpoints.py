import requests
import json
print "Getting Data Via a get request"
r = requests.get("http://104.131.203.11:12000/get_data")
print r.text
print 
print
print "Getting Data Via a post request"
r = requests.post("http://104.131.203.11:12000/get_data")
print r.text
print
print
print "Sending Data"
data = {"Greeting":"Hello there"}
print "Here is the data we will be sending", data
r = requests.post("http://104.131.203.11:12000/send_data/"+json.dumps(data))
print r.text
print 
print
r = requests.get("http://104.131.203.11:12000/view_data")
print r.text

