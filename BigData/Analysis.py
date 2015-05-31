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

#[ak,al,ar,az,co,ct,de,fl,ga,hi,ia,,id,il,in,kn,la,mo,ms,mt,nc,nd,ne,nh,nj,nm,ny]
#print db.crimestats.find()
states=['ca','ky','ma','md','me','mi','mn','oh','or','pa','ri','sc','sd','tn','tx','ut','va','vt','dc','wa','wi','wv','wy','nv','ak','al','ar','az','co','ct','de','fl','ga','hi','ia','id','il','in','kn','la','mo','ms','mt','nc','nd','ne','nh','nj','nm','ny']
with open('data1.csv', 'w') as csvfile:
    fieldnames = ['State','Violent', 'Property','Total','Population']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for s in range(len(states)):
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


    #print "RES=",statistics.mean(res)
        percent=statistics.mean(total)/statistics.mean(pop)*100
        data1[j]={"State":states[s],"Violence":statistics.mean(violent),"Property":statistics.mean(prop),"Percent":percent}     
        Percentage=(statistics.mean(total)/statistics.mean(pop))*100
        Percent[states[s]]=Percentage
        print states[s],"Population MEAN=",statistics.mean(pop)
        print states[s],"Total Crime MEAN=",statistics.mean(total)
        print states[s],"violent MEAN=",statistics.mean(violent)
        print states[s],"violent MEDIAN=",statistics.median(violent)    
        print states[s],"violent Standard Deviation=",statistics.stdev(violent)
        print states[s],"Property MEAN=",statistics.mean(prop)
        print states[s],"Property  MEDIAN=",statistics.median(prop)    
        print states[s],"Property  Standard Deviation=",statistics.stdev(prop)
        print states[s],"Population MEAN=",statistics.mean(violent)
        print "***------------------------------------***"
        print states[s],"PERCENTAGE=",Percentage
        print "***------------------------------------***"
        print "=========================="
        writer.writerow({'State':states[s],'Violent': statistics.mean(violent), 'Property': statistics.mean(prop), 'Total': statistics.mean(total), 'Population': statistics.mean(pop)})
        percent=statistics.mean(total)/statistics.mean(pop)*100
        data1[j]={"State":states[s],"Violence":statistics.mean(violent),"Property":statistics.mean(prop),"Percent":percent}
#print Percent
#print "sorted=",sorted(Percent.iteritems(),key=operator.itemgetter(1))
gg=sorted(Percent.iteritems(),key=operator.itemgetter(1))
#it = iter(sorted(Percent.iteritems()))
#print it.next()
#gg=sorted(Percent.values())
j=1
for k in range(len(gg)):
    
    print "****=========================*****"
    print gg[k]
    

print "state with highest crimerate(Not SAFE)==>",max(Percent.iteritems(), key=operator.itemgetter(1))[0],"=" ,max(Percent.iteritems(),key=operator.itemgetter(1))[1]
print "state with lowest crimerate(SAFE)==>",min(Percent.iteritems(), key=operator.itemgetter(1))[0],"=" ,min(Percent.iteritems(), key=operator.itemgetter(1))[1]
with open('data.json', 'w') as outfile:
    data2="data=",data1
    print data1
    json.dump(data1, outfile)
    print "JSON CREATED"



