#!/usr/bin/env python

import requests
import json

import common

url = 'http://%s/api' % (common.ip)

device_type_json = json.dumps({"devicetype":"python_jf"})
r = requests.post(url, data=device_type_json)
print(r.text)