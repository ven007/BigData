import pymongo
import statistics
from pprint import pprint
from pymongo import MongoClient
connection = MongoClient()
db=connection.crime
collection=db.crimestats



item=collection.find()
violent=[]
prop=[]


#print db.crimestats.find()
states=['us','ca','ky','ma','md','me','mi','mn','oh','or','pa','ri','sc','sd','tn','tx','ut','va','vt','dc','wa','wi','wv','wy','nv']
for s in range(len(states)):
    for doc in collection.find({"State":states[s]}):
        #print doc['Murder']
        violent1=str(doc['Violent']).strip()
        prop1=str(doc['Property']).strip()        
        if(violent1!=''):
         violent2=int(violent1)    
         violent.append(violent2)
        if(prop1!=''):
         prop2=int(prop1)    
         prop.append(prop2)         
        



    #print "RES=",statistics.mean(res)
    print states[s],"violent MEAN=",statistics.mean(violent)
    print states[s],"violent MEDIAN=",statistics.median(violent)    
    print states[s],"violent Standard Deviation=",statistics.stdev(violent)
    print states[s],"Property MEAN=",statistics.mean(prop)
    print states[s],"Property  MEDIAN=",statistics.median(prop)    
    print states[s],"Property  Standard Deviation=",statistics.stdev(prop)    
    print "=========================="



