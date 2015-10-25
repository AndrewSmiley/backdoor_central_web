__author__ = 'pridemai'
import json

data = {}
data['ipaddress']='192.168.1.114'
data['port']='22'
data['username']='root'
data['password']='password'
data['session_start']='6:35'
data['session_end']='9:35'
data['virtual_machine_name']='ubuntu'
data['errors']=''

with open('static/json/data.json', 'w+') as fp:
    data = json.dump(data, fp)
