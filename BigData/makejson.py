import csv
import pymongo
import statistics
import operator
import json
from pprint import pprint
from pymongo import MongoClient
connection = MongoClient()
db=connection.crime
collection=db.crimestats



item=collection.find()
violent=[]
prop=[]
total=[]
pop=[]
Percent={}
data1={}
states=['ca','ky','ma','md','me','mi','mn','oh','or','pa','ri','sc','sd','tn','tx','ut','va','vt','dc','wa','wi','wv','wy','nv']
#print db.crimestats.find()

#fieldnames = ['State','Violent', 'Property','Total','Population']
#writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#writer.writeheader()
for s in range(len(states)):
    #states.keys().index(states[s])
    j=states.index(states[s])
    for doc in collection.find({"State":states[s]}):
        #print doc['Murder']
        violent1=str(doc['Violent']).strip()
        prop1=str(doc['Property']).strip()
        pop1=str(doc['Population']).strip()
        total1=str(doc['Total']).strip() 
        if(violent1!=''):
         violent2=int(violent1)    
         violent.append(violent2)
        if(prop1!=''):
         prop2=int(prop1)    
         prop.append(prop2)         
        if(pop1!=''):
         pop2=int(pop1)    
         pop.append(pop2)         
        if(total1!=''):
         total2=int(total1)    
         total.append(total2) 
    percent=statistics.mean(total)/statistics.mean(pop)*100
    data1[j]={"State":states[s],"Violence":statistics.mean(violent),"Property":statistics.mean(prop),"Percent":percent}
    

with open('data.json', 'w') as outfile:
    data2="data=",data1
    print data1
    json.dump(data1, outfile)
    print "JSON CREATED"


