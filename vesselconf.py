import json

conf={}
conf['host']='127.0.0.1'
conf['port']=8100
conf['stmport']=8000
conf['id']='urn:mrn:stm:service:instance:furuno:imo7917551'
conf['name']='VIS-MadameButterfly'
with open('vessel.conf', 'w') as f:
    f.write(json.dumps(conf))

