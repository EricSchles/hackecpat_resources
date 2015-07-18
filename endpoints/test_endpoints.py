import requests
import json
print "Getting Data Via a get request"
r = requests.get("http://localhost:5000/get_data")
print r.text
print 
print
print "Getting Data Via a post request"
r = requests.post("http://localhost:5000/get_data")
print r.text
print
print
print "Sending Data"
data = {"Greeting":"Hello there"}
print "Here is the data we will be sending", data
r = requests.post("http://localhost:5000/send_data/"+json.dumps(data))
print r.text
