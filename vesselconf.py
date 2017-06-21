import json

conf={}
conf['host']='127.0.0.1'
conf['port']=8100
conf['id']='urn:mrn:stm:service:instance:furuno:imo8016550'
conf['name']='M/V Madame Butterfly'
with open('vessel.conf', 'w') as f:
    f.write(json.dumps(conf))

