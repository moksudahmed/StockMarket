import requests
import sys
import json
from bs4 import BeautifulSoup
from csv import writer
try:
    url="https://www.dse.com.bd/latest_share_price_scroll_l.php"
    response= requests.get(url).text
except:
    sys.exit("Failed to connect!")
soup = BeautifulSoup(response, "html.parser")
tabl = soup.find("table", class_="table")
#print(tabl)
header = []  # Created Empty List
# Extract header row
# for i in tabl.find_all('th'):
#     header.append(i.text)
try:
    with open("dse.json", "w") as f:
        # csv_writer = writer(csv_file)
        # csv_writer.writerow(header) # write header
        
        # Write data to csv file
        for row in tabl.find_all('tr')[1:]:
            td = row.find_all('td')    
        #  r = [i.text.replace('\n','') for i in td[1]]
        
            r = [i.text.replace('\n','') for i in td[1]]
            
            print("%s is %s years old." % (r, td[2].text))
       #     csv_writer.writerow([td[0].text] + r  + [td[2].text] + [td[3].text] + [td[4].text] + [td[5].text] + [td[6].text] + [td[7].text] + [td[8].text] + [td[9].text] + [td[10].text])
            #csv_writer.writerow(r + td[2].text)
        f.write(r)
except:
    sys.exit("Faild to extract data")