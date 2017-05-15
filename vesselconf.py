import json

conf={}
conf['host']='127.0.0.1'
conf['port']=8100
with open('vessel.conf', 'w') as f:
    f.write(json.dumps(conf))

