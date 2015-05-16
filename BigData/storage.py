import urllib
import re
import io
import string
import json
from collections import Counter
from bs4 import BeautifulSoup
#link = "http://www.disastercenter.com/crime/uscrime.htm"
link = "http://www.disastercenter.com/crime/cacrime.htm"
f = urllib.urlopen(link)
myfile = f.read()
soup = BeautifulSoup(myfile)
soup1=soup.find('table')
soup3=str(soup1)
#soup4=soup3[::-1]
#result = re.sub("<.*?>", "", soup3)
#result = re.sub('<div style="text-align: center;">','', soup3)
#result =soup.findAll('<td style="text-align: center;">')
tables = soup.findChildren('table')
my_table = tables[0]
rows = my_table.findChildren('tr')
#rows= re.sub("<.*?>", "", str(rows[149]))
#print(rows[149].findChildren('a'))

##li=rows[149].findChildren('a')
##for i in range(len(li)):       
##	link1= li[i].get('href')
##	#link = "http://www.disastercenter.com/crime/uscrime.htm"
##	f1 = urllib.urlopen(link1)
##	myfile01 = f1.read()
##	soup100 = BeautifulSoup(myfile01)
##	soup101=soup100.find('table', width="100%")
##	soup303=str(soup101)
##	print soup303
	#result = re.sub("<.*?>", "", soup303)
##	for j in range(0,11):
##		Json_result={
##		'Year': result,
##		'Population': result,
##		'Index': result,
##		'Violent':result,
##		'Property':result,
##		'Murder':result,
##		'Rape':result,
##		'Robbery':result,
##		'assault':result,
##		'Burglary':result,
##		'LTheft':result,
##		'VTheft':result
##		}
##		print(Json_result)
##    #print(li[i].get('href'));

##    #print("------------------------------")
##		output=open("out.json","a+")
##		json.dump(r,output, indent=4)
##    #output.write(li[i].get('href'))
##    #output.write("--------")
##		output.close()

li=rows[len(rows)-1].findChildren('a')
print len(rows)
print li
for i in range(len(li)):       
        link1= li[i].get('href')

        #print link1
        f1 = urllib.urlopen(link1)
        myfile01 = f1.read()
        soup100 = BeautifulSoup(myfile01)
        #print "main2=",soup100
        soup101=soup100.find('table', width="100%")
        # print "main=",soup101
        #soup303=str(soup101)
        #print "test-",len(soup101.findChildren('tr'))
        rows = soup101.findChildren('tr')
        if rows!=[]:
                rows = soup101.findChildren('tr')
                print len(rows[2])
                list =dict()
                for m in range(len(rows)):
                        data= str(rows[m].findChildren('td'))
                        striped_data=re.sub("<.*?>", "", data)
                        print len(striped_data)
                        data1=striped_data.split(' ')
                        #print "sd",data1
                        print len(data1)
                        #print "test=",data1[2]



                        list[m] ={'Year':re.sub("[^0-9a-zA-Z]", "", data1[0]),
                                        'Population':re.sub("[^0-9a-zA-Z]", "", data1[1]),
                                        'Total':re.sub("[^0-9a-zA-Z]", "", data1[2] ),
                                        'Violent':re.sub("[^0-9a-zA-Z]", "", data1[3]),
                                        'Property':re.sub("[^0-9a-zA-Z]", "", data1[4]),
                                        'Murder':re.sub("[^0-9a-zA-Z]", "", data1[5]),
                                        'Rape':re.sub("[^0-9a-zA-Z]", "", data1[6]),
                                        'Robbery':re.sub("[^0-9a-zA-Z]", "", data1[7]),
                                        'assault':re.sub("[^0-9a-zA-Z]", "", data1[8]),
                                        'Burglary':re.sub("[^0-9a-zA-Z]", "", data1[9]),
                                        'LTheft':re.sub("[^0-9a-zA-Z]", "", data1[10]),
                                        'VTheft':re.sub("[^0-9a-zA-Z]", "", data1[11])
                                        }
        else:
                print "====NO TYPE==="


print "dict--",list
output=open("out.json","w")
json.dump(list,output, indent=4)
output.close()
