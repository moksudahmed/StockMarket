import requests
import sys
import json
import stockurl
import threading
from bs4 import BeautifulSoup
from csv import writer

def connection():
    try:    
        response= requests.get(stockurl.get_url()).text    
    except:
        sys.exit("Failed to connect!")

    soup = BeautifulSoup(response, "html.parser")
    tabl = soup.find("table", class_="table")
    return tabl

def write_json(ls_dict):
    json_object = json.dumps(ls_dict, indent=4)
    print(json_object)
    # Writing to sample.json
    with open("stockdata.json", "w") as outfile:
        outfile.write(json_object)

def remove_character(line):
    line = line.replace('\r', '')
    line = line.replace('\t', '')
    line = line.replace('\n', '')
    return line

def scrap():
    
    tabl = connection()

    try:
            ls_dict = []
            # Extract data from html table 
            for row in tabl.find_all('tr')[1:]:
                ds = {"SL":"",
                    "TRADING_CODE":"",
                    "LTP":"",
                    "HIGH":"",
                    "LOW":"",
                    "CLOSE":"",
                    "YCP":"",
                    "CHANGE":"",
                    "TRADE":"",
                    "VALUE":"",
                    "VOLUME":""
                    }
                td = row.find_all('td')            
                # Update data to a dictonary
                ds.update({ "SL":td[0].text,
                            "TRADING_CODE":remove_character(td[1].text), 
                            "LTP" : td[2].text, 
                            "HIGH" : td[3].text,
                            "LOW" : td[4].text,
                            "CLOSE" : td[5].text,
                            "YCP" : td[6].text,
                            "CHANGE" : td[7].text,
                            "TRADE" : td[8].text,
                            "VALUE" : td[9].text,
                            "VOLUME" : td[10].text
                        })
                #Generate a list of dictonary
                ls_dict.append(ds)
            # Write a list to a JSON file
            write_json(ls_dict)
        
    except:
        sys.exit("Faild to extract data")

scrap()

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

# using
setInterval(scrap,10)