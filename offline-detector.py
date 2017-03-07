#!/usr/bin/env python

import requests
import json
import httplib
import time

import common

def have_internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=3)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

def set_light_on_status(status):
	try:
		url = 'http://%s/api/%s/lights/3/state' % (common.ip, common.user_name)
		on_state_json = json.dumps({"on": status})
		r = requests.put(url, data=on_state_json, timeout=3)
	except:
		print("failed to change light state" )


while True:
	time.sleep(0.5) 
	if have_internet():
		print("online")
		set_light_on_status(True)
	else:
		print("offline")
		set_light_on_status(False)