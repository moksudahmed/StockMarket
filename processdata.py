import os
from pickle import FALSE, TRUE
import datetime
from datetime import datetime
import scraper
import json

def get_stock_data():
    with open('stockdata.json', 'r') as f:      
      data = json.load(f)     
    return data    
    
def isModified():  
    # Path to the file
    path = "stockdata.json"
    # file modification timestamp of a file
    m_time = os.path.getmtime(path)
    # convert timestamp into DateTime object
    dt_m = datetime.fromtimestamp(m_time)
    #print('Last Modified on:', dt_m)    
    # in hours:minutes:seconds format
    delta = datetime.now() - dt_m        
    if delta.total_seconds() >= 300:
       scraper.scrap()
       return TRUE
    else:
       return FALSE


