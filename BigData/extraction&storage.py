from lxml import html
import requests
import re
import json
from pymongo import MongoClient
import time
connection = MongoClient()
db=connection.crime
collection=db.crimestats
states=['ca','ky','ma','md','me','mi','mn','oh','or','pa','ri','sc','sd','tn','tx','ut','va','vt','dc','wa','wi','wv','wy','nv','ak','al','ar','az','co','ct','de','fl','ga','hi','ia','id','il','in','kn','la','mo','ms','mt','nc','nd','ne','nh','nj','nm','ny']
for s in range(len(states)):
    print states[s]
    link1="http://www.disastercenter.com/crime/"+states[s]+"crime.htm"

    startTime = time.time()
    page = requests.get("http://www.disastercenter.com/crime/uscrime.htm")

    tree = html.fromstring(page.text)


    tables = [tree.xpath('//table/tbody/tr[2]/td/center/center/font/table/tbody')]

    tabs = []

    for table in tables:
        tab = []
        for row in table:
            for col in row:
                var = col.text_content()
                var = var.strip().replace(" ", "")
                var = var.split('\n')
                if re.match('^\d{4}$', var[0].strip()):
                    db.crimestats.insert({"State":states[s],
                    "Year":re.sub("[^0-9]", "",var[0].strip()),
                    "Population": re.sub("[^0-9]", "",var[1].strip()),
                    "Total":re.sub("[^0-9]", "", var[2].strip()),
                    "Violent":re.sub("[^0-9]", "",var[3].strip()),
                    "Property": re.sub("[^0-9]", "",var[4].strip()),
                    "Murder":re.sub("[^0-9]", "", var[5].strip()),
                    "Forcible_Rape": re.sub("[^0-9]", "",var[6].strip()),
                    "Robbery":re.sub("[^0-9]", "",var[7].strip()),
                    "Aggravated_Assault": re.sub("[^0-9]", "",var[8].strip()),
                    "Burglary": re.sub("[^0-9]", "",var[9].strip()),
                    "Larceny_Theft": re.sub("[^0-9]", "",var[10].strip()),
                    "Vehicle_Theft": re.sub("[^0-9]", "",var[11].strip())})

print "DATA DUMP1 SUCCESS"
                    
        



