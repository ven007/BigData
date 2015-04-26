import urllib
import re
import io
from collections import Counter
from bs4 import BeautifulSoup
link = "http://www.disastercenter.com/crime/uscrime.htm"
f = urllib.urlopen(link)
myfile = f.read()
soup = BeautifulSoup(myfile)
soup1=soup.find('table', width="100%")
soup3=str(soup1)
result = re.sub("<.*?>", "", soup3)
print(result)
output=open("output.txt","w")
output.write(result)
output.close()
